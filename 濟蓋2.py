from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# key = RSA.generate(2048)
privateKey = open('private.pem').read()
publicKey = open('public.pem').read()

message = "Hello World!"
message = str.encode(message)

RSApublicKey = RSA.importKey(publicKey)
OAEP_cipher = PKCS1_OAEP.new(RSApublicKey)
encryptedMsg = OAEP_cipher.encrypt(message)

print('Encrypted text:', encryptedMsg)

RSAprivateKey = RSA.importKey(privateKey)
OAEP_cipher = PKCS1_OAEP.new(RSAprivateKey)
decryptedMsg = OAEP_cipher.decrypt(encryptedMsg)


print('The original text:', decryptedMsg)


with open("en.txt", "wb") as f:
    f.write(encryptedMsg)
