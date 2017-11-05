class Node:

    def __init__(self , c = None , count = 0 , lSon = None , rSon = None):
        self.__father = None
        self.__leftSon = lSon
        self.__rightSon = rSon
        self.__presentation = ""
        self.__c = str(c)
        self.__count = count
        if count == 0:
            self.__count = lSon.get_count() + rSon.get_count()

    def get_father(self):
        return self.__father

    def get_left_son(self):
        return self.__leftSon

    def get_right_son(self):
        return self.__rightSon

    def get_presentation(self):
        return self.__presentation
    
    def get_char(self):
        return self.__c
    
    def get_node_height(self):
        return self.__height
    
    def get_count(self):
        return self.__count
    
    def set_node_height(self , height):
        self.__height = height

    def set_left_son(self,n):
        self.__leftSon = n

    def set_right_son(self,n):
        self.__rightSon = n

    def set_father(self,n):
        self.__father = n
    
    def set_presentation(self,c):
        self.__presentation = c
    
    def is_leaf(self):
        return self.__leftSon == None and self.__rightSon == None

