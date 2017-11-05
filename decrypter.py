
class Decrypter:
    
    def __init__(self,p = None):
        self.__presentation = p
    
    def decrypt_file(self,f):
        # print("pres!")
        # print(self.__presentation)
        f.seek(0,0)
        content = f.read()
        f.seek(0,0)
        c = f.read(1)
        while c:
            if self.__presentation.has_key(c):
                content = content.replace(c,self.__presentation[c],1)
                c = ""
            c += f.read(1)
        print("content\n" + content)
        f.seek(0)
        f.truncate()
        f.write(content)