from decrypter import Decrypter
class Encrypter:
    
    def __init__(self,charPresent = None):
        self.__presentation = charPresent
    
    def encrypt_file(self,f):
        # print("pres!")
        # print(self.__presentation)
        f.seek(0,0)
        content = f.read()
        f.seek(0,0)
        c = f.read(1)
        while c:
            try:
                # print("char " + self.__presentation[c])
                content = content.replace(c,self.__presentation[c])
            except KeyError:
                pass
            c = f.read(1)
            
        f.seek(0,0)
        print("content:\n" + content)
        f.write(content)
        
    def get_decrypt_char(self):
        return {val:key for key,val in self.__presentation.iteritems()}

# encrypter = Encrypter({'a':'0' , 'b':'1' , 'c' : '2'})
# f = open('./samp.txt','r+')
# encrypter.encrypt_file(f)
# decrypter = encrypter.get_decrypter()
# decrypter.decrypt_file(f)

