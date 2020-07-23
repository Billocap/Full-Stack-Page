import socket
import threading

from Modules.httphandler.httprequest import httprequest
from Modules.httphandler.httpresponse import httpresponse

def baseresponse(request, response):
    basebody = """
    <style>
    * {padding:0px;margin:0px;font-family:Helvetica;font-weight:normal;font-size:50px;}
    h1 {width:100vw;height:100vh;display:flex;align-items:center;justify-content:center;}
    </style>
    <h1>Route Not Defined</h1>
    """

    response.setheader(
        {
            'Content-Length':str(len(basebody)),
            'Content-Type':'text/html; text/xml'
        }
    )
    response.setbody(basebody)

def handleclient(self, client, action = baseresponse):
    request = httprequest()
    request.parserequest(client.recv(self.buffersize))
    response = httpresponse()
    try:
        (self.routes[request.method][request.path])(request,response)
    except:
        action(request,response)
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
    def __init__(self, ip = '0.0.0.0', maxcon = 10, buffersize = 1024):
        self.ip = ip
        self.header = {}
        self.maxcon = maxcon
        self.buffersize = buffersize
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
    
    def listen(self, action = baseresponse, port = 9000):
        serverthread = threading.Thread(target=serverhandler,args=(self,port,action,))
        serverthread.start()

    def get(self, path, action):
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