from Modules.filehandler import filehandler
from Modules.httphandler.httpserver import httpserver

server = httpserver()

def root(request, response):
    response.xml(filehandler.readbytes('./Source/index.html'))

def mainsheet(request, response):
    response.setheader({'Content-Type':'text/css'})
    response.setbody(filehandler.readbytes('./Source/Styles/main.css'))

def mainscript(request, response):
    response.setheader({'Content-Type':'text/javascript'})
    response.setbody(filehandler.readbytes('./Source/Scripts/main.js'))

def getxml(request, response):
    response.xml(filehandler.readbytes('./Source/Pages'+request.path))

server.get('/',root)
server.get('/Styles/main.css',mainsheet)
server.get('/Scripts/main.js',mainscript)

server.get('r/(home|about|share|search)\.html',getxml)

server.listen(port = 8080)