from huffman_tree import HuffmanTree,build_tree
from encrypter import Encrypter
from decrypter import Decrypter
from char_counter import CharCounter
while True:
    print("Welcome to huffman tree decrpter encrypter")
    #get file path
    fPath = raw_input("please enter the file path\n")
    file = open(fPath,"r+")
    #get count chars in file
    char = file.read(1)
    charCounter = CharCounter()
    while char:
        charCounter.add_char(char)
        char = file.read(1)
    # print("char count")
    # print(charCounter.get_char_counter())
    #init huffman tree
    huffmanTree = build_tree(charCounter.get_char_counter())
    # huffmanTree.preorder_print(huffmanTree.get_root())
    #get presentation from tree
    presentation = {}
    huffmanTree.get_tree_nodes(huffmanTree.get_root(),presentation)
    print("presentation")
    print(presentation)
    # #init encryp
    encrypter = Encrypter(presentation)
    print(encrypter.get_decrypt_char())
    doEncryption = raw_input("encrypt file y/n\n")
    if doEncryption == "y":
        encrypter.encrypt_file(file)
    # #init decrypter
    decrypter = Decrypter(encrypter.get_decrypt_char())
    doDecryption = raw_input("decrypt file y/n\n")
    if doDecryption == "y":
        decrypter.decrypt_file(file)
    #check if user want to quit or no
    quit = raw_input("exit y/n\n")
    if quit == "y":
        file.close()
        break
print("Thank you for using huffman tree")
exit(0)


