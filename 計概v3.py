#
#   This is a just print hello world 
#   date：03-Nov-2022
#   Author：MAXKIRITO
#

import os
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from pyfiglet import Figlet

class how_to_print_a_hello_world:
    def __init__(self):
        
        self.privateKey = open('private.pem').read()
        self.publicKey = open('public.pem').read()
        
        self.a = "Hello World!"
        self.b = ["H","e","l","l","o"," ","W","o","r","l","d","!"]
        self.c = f = Figlet(font="slant", width=300) 
        self.d = open("helloworld.txt", "r")
        self.e = open("en.txt",'rb').read()
        self.z = os.system("echo Hello World!")
        
    def general_print_hello_world(self):
        
        print(self.a)
        
    def use_list_to_print_hello_world(self):
        
        for i in range(len(self.b)):
            print(self.b[i],end="")
        print()
        
    def text_art(self):
        
        print(self.c.renderText(self.a))
    
    def read_a_file_and_print_content(self):
        
        print(self.d.read())
        
    def decrypted_a_encrypted_text_file(self):
        
        RSAprivateKey = RSA.importKey(self.privateKey)
        OAEP_cipher = PKCS1_OAEP.new(RSAprivateKey)
        decryptedMsg = OAEP_cipher.decrypt(self.e)
        print(decryptedMsg)

    def call_os_to_print_hello_world(self):
        
        print(self.z)