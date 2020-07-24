import socket
import threading
import re

from Modules.httphandler.httprequest import httprequest
from Modules.httphandler.httpresponse import httpresponse
from Modules.httphandler.information.methods import methods

def baseresponse(request, response):
    basebody = """
    <style>
    * {padding:0px;margin:0px;font-family:Helvetica;font-weight:normal;font-size:50px;}
    h1 {width:100vw;height:100vh;display:flex;align-items:center;justify-content:center;}
    </style>
    <h1>Route Not Defined</h1>
    """

    response.xml(basebody)

def methodnotallowed(request, response):
    basebody = """
    <style>
    * {padding:0px;margin:0px;font-family:Helvetica;font-weight:normal;font-size:50px;}
    h1 {width:100vw;height:100vh;display:flex;align-items:center;justify-content:center;}
    </style>
    <h1>Method Not Allowed</h1>
    """

    response.setstatus(405)
    response.xml(basebody)

def handleclient(self, client, action = baseresponse):
    request = httprequest()
    request.parserequest(client.recv(self.buffersize))
    response = httpresponse()
    
    if request.method in self.methods:
        try:
            (self.routes[request.method][request.path])(request,response)
        except:
            action(request, response)
            for regex in self.regexroutes[request.method].keys():
                if re.search(regex[2:], request.path):
                    (self.routes[request.method][regex])(request,response)
                    break
    else:
        methodnotallowed(request, response)
    client.send(response.getresponse())
    client.close()

def serverhandler(self, port, action = baseresponse):
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((self.ip,port))
    server.listen()

    while True:
        client, addr = server.accept()

        clientthread = threading.Thread(target=handleclient,args=(self,client,action,))
        clientthread.start()

class httpserver:
    def __init__(self, ip = '0.0.0.0', maxcon = 10, buffersize = 1024, methods = methods):
        self.ip = ip
        self.header = {}
        self.maxcon = maxcon
        self.buffersize = buffersize
        self.methods = methods
        self.routes = {
            'GET'    : {},
            'POST'   : {},
            'PATCH'  : {},
            'DELETE' : {},
            'HEAD'   : {},
            'CONNECT': {},
            'OPTIONS': {},
            'TRACE'  : {},
            'PUT'    : {}
        }

        self.regexroutes = self.routes
    
    def listen(self, action = baseresponse, port = 9000):
        serverthread = threading.Thread(target=serverhandler,args=(self,port,action,))
        serverthread.start()

    def get(self, path, action):
        if path[0] == 'r':
            self.regexroutes['GET'][path] = action
        else:
            self.routes['GET'][path] = action

    def post(self, path, action):
        self.routes['POST'][path] = action
    
    def patch(self, path, action):
        self.routes['PATCH'][path] = action

    def delete(self, path, action):
        self.routes['DELETE'][path] = action

    def head(self, path, action):
        self.routes['HEAD'][path] = action

    def connect(self, path, action):
        self.routes['CONNECT'][path] = action

    def options(self, path, action):
        self.routes['OPTIONS'][path] = action

    def trace(self, path, action):
        self.routes['TRACE'][path] = action

    def put(self, path, action):
        self.routes['PUT'][path] = action