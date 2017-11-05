from tree_node import Node
import operator
class HuffmanTree:

    def __init__(self):
        self.__r = None
        self.__tHeight = 0

    def get_root(self):
        return self.__r
    
    def set_root(self,r):
        self.__r = r    
    
    def get_height(self):
        return self.__tHeight

    def add_left_son(self,root,leaf):
        root.set_left_son(leaf)
        leaf.set_father(root)
        leaf.set_node_height(root.get_node_height() + 1)
        if root.get_presentation() != None:
            leaf.set_presentation(root.get_presentation() + "0")
        else:
            leaf.set_presentation("0")
    
    def add_right_son(self,root,leaf):
        root.set_right_son(leaf)
        leaf.set_father(root)
        leaf.set_node_height(root.get_node_height() + 1)
        if root.get_presentation() != None:
            leaf.set_presentation(root.get_presentation() + "1")
        else:
            leaf.set_presentation("1")
            
    def get_tree_height(self,root,func):
        if root.is_leaf():
            return 0
        elif root.get_left_son() != None and root.get_right_son() != None:
            return func(1 + self.get_tree_height(root.get_left_son(),func),1 + self.get_tree_height(root.get_right_son(),func))
        elif root.get_left_son() != None:
            return 1 + self.get_tree_height(root.get_left_son(),func)
        elif root.get_right_son() != None:
            return 1 + self.get_tree_height(root.get_right_son(),func)
            
    def set_tree_height(self):
        self.__r = self.get_tree_height(self.__r,max)
        
    def update_tree_height(self,height):
        self.__tHeight = height;
        
    def binary_add(self,root,n1,n2):
        #we went to empty node
        if root == None:
            return False
        elif self.get_height() == root.get_node_height():
            return False
        elif root.is_leaf() and root.get_node_height() < self.get_height():
            self.set_left_right_son(root,n1,n2)
            return True
        else:#we should add the nodes
            return self.binary_add(root.get_left_son(),n1,n2) or self.binary_add(root.get_right_son(),n1,n2)
            
            
        
    def set_left_right_son(self,root,n1,n2):
        self.add_left_son(root,n1)
        self.add_right_son(root,n2)
    
    def get_most_left_son(self,root):
        if root.is_leaf():
            return root
        else:
            return self.get_most_left_son(root.get_left_son())
    
    def add_nodes_to_tree(self,n1,n2):
        if not self.binary_add(self.get_root(),n1,n2):
            mostLeftLeaf = self.get_most_left_son(self.get_root())
            self.set_left_right_son(mostLeftLeaf,n1,n2)
            self.update_tree_height(self.get_height() + 1)

    def preorder_print(self,root):
        if root.is_leaf():
            return root
        else:
            print("###")
            if root == self.get_root():
                print("root")
            else:
                print(root.get_char())
            print(root.get_left_son().get_char() + " prese " + root.get_left_son().get_presentation())
            print(root.get_right_son().get_char() + " prese " + root.get_right_son().get_presentation())
            print("###")
            self.preorder_print(root.get_left_son())
            self.preorder_print(root.get_right_son())
            
    def get_tree_nodes(self,root,presentation):
        if root.is_leaf():
            presentation[root.get_char()] = root.get_presentation()
            return
        else:
            self.get_tree_nodes(root.get_left_son(),presentation)
            self.get_tree_nodes(root.get_right_son(),presentation)
            
    def set_presentation(self,root):
        if root.is_leaf():
            return
        else:
            root.get_left_son().set_presentation(root.get_presentation() + "0")
            root.get_right_son().set_presentation(root.get_presentation() + "1")
            self.set_presentation(root.get_left_son())
            self.set_presentation(root.get_right_son())
        
def build_tree(presentation):
        #init new tree
    huffmanT = HuffmanTree()
    #check if presentation length is even
    chars = presentation.keys()
    if len(chars) % 2 == 1:
        values = presentation.values()
        presentation[None] = max(values) + 1
    #sort the key by values
    sortedP = sort_dic(presentation)
    nodeQueue = make_node_queue(sortedP)
    while(1 < len(nodeQueue)):
        n1 = nodeQueue.pop()
        n2 = nodeQueue.pop()
        # print("lson " + str(n1.get_count()) + " rson " + str(n2.get_count()))
        father = Node("",0,n1,n2)
        nodeQueue.append(father)
        # print("father " + str(father.get_count()))
        #sort queue
        sort_queue(nodeQueue)
    huffmanT.set_root(nodeQueue.pop())
    huffmanT.set_presentation(huffmanT.get_root())
    return huffmanT

def make_node_queue(nList):
    queue = []
    for cell in nList:
        print(str(cell[0]) + " " + str(cell[1]))
        n = Node(cell[0],cell[1])
        queue.append(n)
    return queue

def sort_dic(presentation):
    sortedP = sorted(presentation.items(), key=operator.itemgetter(1))
    sortedP = list((sortedP))
    return sortedP

def sort_queue(queue):
    queue.sort(key=lambda x: x.get_count(), reverse=True)
        
# t = HuffmanTree()
# n1 = Node("1")
# n2 = Node("2")
# n3 = Node("3")
# n4 = Node("4")
# n5 = Node("5")
# n6 = Node("6")
# n7 = Node("7")
# n8 = Node("8")
# # t.add_right_son(t.get_root(),n1)
# # t.add_right_son(t.get_root(),n2)
# # t.add_left_son(t.get_root(),n3)
# # t.add_right_son(t.get_root(),n4)
# # print(t.get_root().get_right_son().get_right_son().get_father().get_presentation())
# # print(t.get_root().get_left_son().get_presentation())
# # t.set_tree_height()
# # print(t.get_height())
# t.add_nodes_to_tree(n1,n2)
# # print("left root son " + str(t.get_root().get_left_son().get_presentation()) + " right root son " + str(t.get_root().get_right_son().get_presentation()))
# # print("tree height " + str(t.get_height()))
# t.add_nodes_to_tree(n3,n4)
# # print("tree height " + str(t.get_height()))
# # print("left left root son " + str(t.get_root().get_left_son().get_left_son().get_presentation()) + " left right root son " + str(t.get_root().get_left_son().get_right_son().get_presentation()))
# t.add_nodes_to_tree(n5,n6)
# # print(t.get_root().get_left_son().get_node_height())
# # print("tree height " + str(t.get_height()))
# # print("right left root son " + str(t.get_root().get_right_son().get_left_son().get_presentation()) + " right right root son " + str(t.get_root().get_right_son().get_right_son().get_presentation()))
# t.add_nodes_to_tree(n7,n8)
# # print("left left left root son " + str(t.get_root().get_left_son().get_left_son().get_left_son().get_presentation()) + " left left right root son " + str(t.get_root().get_left_son().get_left_son().get_right_son().get_presentation()))
# # t.preorder_print(t.get_root())
# p = {}
# t.get_tree_nodes(t.get_root(),p)
# print(p)
# print("//////////////")
# presentation = {"a":1,"b":2,"c":3}
# tree = init_tree_from_presentation(presentation)
# tree.preorder_print(tree.get_root())
# presentation = {}
# tree.get_tree_nodes(tree.get_root(),presentation)
# print(presentation)


    
