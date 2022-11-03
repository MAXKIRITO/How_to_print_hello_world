import os
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from pyfiglet import Figlet

privateKey = open('private.pem').read()
publicKey = open('public.pem').read()

a = "Hello World!"
b = ["H","e","l","l","o"," ","W","o","r","l","d","!"]
z = os.system("echo Hello World!")
d = open("helloworld.txt", "r")
e = open("en.txt",'rb').read()
c = f = Figlet(font="slant", width=300) 


print("Hello World!")

print(a)

for i in range(len(b)):
  print(b[i],end="")
print()

print(c.renderText(a))

print(d.read()) 

RSAprivateKey = RSA.importKey(privateKey)
OAEP_cipher = PKCS1_OAEP.new(RSAprivateKey)
decryptedMsg = OAEP_cipher.decrypt(e)
print(decryptedMsg)

print(z)
