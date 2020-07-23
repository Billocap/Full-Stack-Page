from Modules.filehandler import filehandler
from Modules.httphandler.httpserver import httpserver

server = httpserver()

server.listen(port = 8080)