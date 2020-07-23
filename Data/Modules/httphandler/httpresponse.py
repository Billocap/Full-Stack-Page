from Modules.httphandler.information.responses import responses

def inttobyte(integer):
    return str.encode(str(integer))

def strtobyte(string):
    return str.encode(string)

class httpresponse:
    def __init__(self):
        self.protocol = b'HTTP/1.1'
        self.status = b'200'
        self.message = strtobyte(responses['200'])
        self.header = {}
        self.body = b''

    def setbody(self, body = ''):
        if type(body) == str:
            self.body = strtobyte(body)
        else:
            self.body = body

    def setstatus(self, status, message=''):
        self.status = inttobyte(status)
        try:
            self.message = message if strtobyte(message) else strtobyte(responses[self.status.decode()])
        except:
            self.message = message if strtobyte(message) else b'No Message'

    def setheader(self, header):
        if type(header) == dict:
            for key in header.keys():
                self.header[key] = header[key]
        else:
            print("The Must Be Of Type Dict")
    
    def setfullheader(self, status, message = '', header={}):
        self.setstatus(status, message)
        self.setheader(header)
    
    def getresponse(self):
        parse = b''
        
        for key in self.header.keys():
            parse += strtobyte(key) + b': ' + strtobyte(self.header[key]) + b'\n'
        parse += b'\n'

        response = self.protocol + b' ' + self.status + b' ' + self.message
        return response + b'\n' + parse + self.body + b'\n\n'
    
    def getstrresponse(self):
        return self.getresponse().decode()