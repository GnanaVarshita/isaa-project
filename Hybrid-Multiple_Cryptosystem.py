import secrets
from Crypto.Cipher import AES
import rsa
def keys():
    global aeskey, publickey, privatekey
    #key generation
    aeskey = secrets.token_bytes(32)
    print("\nAES PUBLIC KEY: ",aeskey)
    publickey, privatekey = rsa.newkeys(1024)
    print("\nRSA PUBLIC KEY: ",publickey)
    print("\nRSA PRIVATE KEY: ",privatekey)
    
#input

# Specify the path to the input file
file_path = "input_part4.enc"

# Initialize an empty variable to store the content of the file
file_content = ""

# Open the file and read its content
try:
    with open(file_path, 'r') as file:
        file_content = file.read()
        print("File content read successfully.")
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

# Now 'file_content' variable contains the content of the file
print("File Content:")
print(file_content)

message=file_content

keys()
def encrypt():
    global nonce,enc,cipherkey
    #aes encryption
    cipherAESe=AES.new(aeskey,AES.MODE_GCM)
    nonce=cipherAESe.nonce
    ciphertext=cipherAESe.encrypt(message.encode("utf-8"))
    print("\n AES ciphertext:",ciphertext)
    #rsa encryption
    enc= rsa.encrypt(ciphertext,publickey)
    print("\n encrypted text by rsa:", enc)
    #encrypting aes key
    cipherkey=rsa.encrypt(aeskey,publickey)
    print("\n Encrypted AES KEY: ",cipherkey)

def decrypt():
    #decrypting aes key
    dicipheredkey =rsa.decrypt(cipherkey,privatekey)
    print("\n Decrypted AES KEY: ",dicipheredkey)
    #rsa decryption
    dec= rsa.decrypt(enc, privatekey)
    print("\n decrypted by rsa:", dec)
    #aes decryption
    cipherAESd=AES.new(dicipheredkey,AES.MODE_GCM,nonce=nonce)
    decrypted=cipherAESd.decrypt(dec).decode("utf-8")
    print("\ndecrypted message by aes:",decrypted)
    with open("4.enc", "w", encoding="utf-8") as file:
        file.write(decrypted)
        print("Decrypted text saved to '4.enc'.")
encrypt()
decrypt()
