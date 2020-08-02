from Modules.httphandler.information.methods import methods
from Modules.httphandler.information.mimetypes import mimetypes

def parseInformation(query,partition,separator):
    c = 0
    result = {}

    parse = ''
    paramether = ''

    while c < len(query):
        char = query[c]

        if char == partition:
            paramether = parse
            result[parse] = ''
            parse = ''
            c += 1
            continue
        elif char == separator:
            if paramether:
                result[paramether] = parse
                paramether = ''
            else:
                result[parse] = ''
            
            parse = ''
            c += 1
            continue
        else:
            parse += char
        
        c += 1

    if paramether:
        result[paramether] = parse
        paramether = ''
    else:
        result[parse] = ''

    return result

class httprequest:
    def __init__(self):
        self.method = 'GET'
        self.path = ''
        self.mimetype = ''
        self.query = {}
        self.index = ''
        self.protocol = ''
        self.header = {}
        self.body = ''

    
    def parserequest(self, request):
        if type(request) == bytes:
            request = request.decode()
        elif type(request) != str:
            print("Request Must Be Of Type String or Bytes")

        parse = ''
        
        n = 0
        while n < len(request):
            char = request[n]

            if char == ' ' and parse in methods:
                self.method = parse
                parse = ''
            elif char == '/' and not self.path:
                while request[n] != '?' and request[n] != '#' and request[n] != ' ':
                    if request[n] == '%':
                        parse += chr(int(request[n+1:n+3],16))
                        n += 2
                    else:
                        parse += request[n]
                    n += 1
                self.path = parse
                try:
                    self.mimetype = mimetypes[parse.partition('.')[2]]
                except:
                    pass
                parse = ''
                continue
            elif char == '?':
                n += 1
                while request[n] != '#' and request[n] != ' ':
                    if request[n] == '%':
                        parse += chr(int(request[n+1:n+3],16))
                        n += 2
                    else:
                        parse += request[n]
                    n += 1
                self.query = parseInformation(parse,'=','&')
                parse = ''
                continue
            elif char == '#':
                n += 1
                while request[n] != ' ':
                    if request[n] == '%':
                        parse += chr(int(request[n+1:n+3],16))
                        n += 2
                    else:
                        parse += request[n]
                    n += 1
                self.index = parse
                parse = ''
                continue
            elif char == '\n' and not self.protocol:
                self.protocol = parse[1:]
                parse = ''
                n += 1
                continue
            elif char == '\r':
                n += 1
                continue
            elif '\n\n' in parse:
                self.header = parseInformation(parse.replace('\n\n',''),':','\n')
                parse = ''
                continue
            else:
                parse += char

            n += 1

        self.body = parse.replace('\n\n','')