import codecs

class filehandler:
    @staticmethod
    def read(path):
        try:
            filedesc = open(path,'r','utf-8')
            filebuffer = filedesc.read()
            filedesc.close()
        except:
            filedesc = codecs.open(path,'r')
            filebuffer = filedesc.read()
            filedesc.close()

        return filebuffer

    @staticmethod
    def readbytes(path):
        try:
            filedesc = open(path,'rb','utf-8')
            filebuffer = filedesc.read()
            filedesc.close()
        except:
            filedesc = codecs.open(path,'rb')
            filebuffer = filedesc.read()
            filedesc.close()

        return filebuffer

    @staticmethod
    def write(path, string):
        try:
            filedesc = open(path,'w','utf-8')
            filebuffer = filedesc.write(string)
            filedesc.close()
        except:
            filedesc = codecs.open(path,'w')
            filebuffer = filedesc.write(string)
            filedesc.close()

    @staticmethod
    def writebytes(path, bytestring):
        try:
            filedesc = codecs.open(path,'wb','utf-8')
            filebuffer = filedesc.write(bytestring)
            filedesc.close()
        except:
            filedesc = open(path,'wb')
            filebuffer = filedesc.write(bytestring)
            filedesc.close()

    @staticmethod
    def append(path, string):
        try:
            filedesc = open(path,'a','utf-8')
            filebuffer = filedesc.write(string)
            filedesc.close()
        except:
            filedesc = codecs.open(path,'a')
            filebuffer = filedesc.write(string)
            filedesc.close()

    @staticmethod
    def appendbytes(path, bytestring):
        try:
            filedesc = codecs.open(path,'ab','utf-8')
            filebuffer = filedesc.write(bytestring)
            filedesc.close()
        except:
            filedesc = open(path,'ab')
            filebuffer = filedesc.write(bytestring)
            filedesc.close()