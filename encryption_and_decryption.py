#will need to pip install cryptodome
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP


'''
encrpytion: takes a file or full file path and a public key enrypts the file\
file: either a file or full file path
public key: the public key used for encryption
uses RSA-SSH2 encryption and OEAP padding
'''
def encryption(file, publickey):
    #open and read the files data
    encfile = open(file, 'rb')
    data = encfile.read()
    encfile.close()
    #generate the cipher using the public key
    cipher = PKCS1_OAEP.new(publickey)
    #encrypt the data
    data = cipher.encrypt(data)
    #open the file again for writing
    encfile = open(file, 'wb')
    #write the encrypted data
    encfile.write(data)
    encfile.close()
    
    return
'''
decrytion: takes a file or full file path and a private key decrypts the file
file: either a file or full file path
public key: the private key used for decryption
uses RSA-SSH2 encryption and OEAP padding
'''   
def decryption(file, privatekey):
    #open the file and read its encrypted data
    decfile = open(file, 'rb')
    data = decfile.read()
    decfile.close()
    #generate our decryption cipher using the private key
    cipher = PKCS1_OAEP.new(privatekey)
    #decrypt the data
    data = cipher.decrypt(data)
    #open the file again for writing
    decfile = open(file, 'wb')
    #write the decrypted data
    decfile.write(data)
    decfile.close()
    return
    
if "__main__" == __name__:
    #open the public key file and get the public key 
    publicfile = open('Path_to_public_key\\Public Key', 'r')
    publickey = publicfile.read()
    publickeydata = RSA.importKey(publickey)
    #open the private key file and get the private key
    privatefile = open('Path_to_private_key\\Private Key', 'r')
    privatekey = privatefile.read()
    privatekeydata = RSA.importKey(privatekey)
    
    #call the encryption or decryption function
    encryption('path_to_file\\filename.extension', publickeydata)
    decryption('path_to_file\\filename.extension', privatekeydata)
    exit()