#
#   This is a just print hello world
#   date：03-Nov-2022
#   Author：MAXKIRITO
#
#
#         __  __     ____         _       __           __    ____
#        / / / /__  / / /___     | |     / /___  _____/ /___/ / /
#       / /_/ / _ \/ / / __ \    | | /| / / __ \/ ___/ / __  / /
#      / __  /  __/ / / /_/ /    | |/ |/ / /_/ / /  / / /_/ /_/
#     /_/ /_/\___/_/_/\____/     |__/|__/\____/_/  /_/\__,_(_)
#
#
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
        self.b = ["H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d", "!"]
        self.c = f = Figlet(font="slant", width=300)
        self.d = open("helloworld.txt", "r")
        self.e = open("en.txt", 'rb').read()
        self.z = os.system("echo Hello World!")

    def general_print_hello_world(self):

        print(self.a)

    def use_list_to_print_hello_world(self):

        for i in range(len(self.b)):
            print(self.b[i], end="")
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
        
    def use_some_magic_to_print_hello_world(slef):
        print(''.join([chr(round(-(79*x**12)/31933440+(409*x**11)/3193344-(21697*x**10)/14515200-(67877*x**9)/1451520+(88163*x**8)/46080-(1029115*x**7)/32256+(4562068069*x **
              6)/14515200-(2884823503*x**5)/1451520+(1191723787*x**4)/145152-(1580287133*x**3)/72576+(1391865319*x**2)/39600-(170471681*x)/5544+10940)) for x in range(1, 14)]))
