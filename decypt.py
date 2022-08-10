import os
from cryptography.fernet import Fernet

files = [] 

for file in os.listdir(): # list every file in directory
    if file == "voldemort.py" or file == "thekey.key" or file == "decypt.py":
        continue
    if os.path.isfile(file):# also do not take folder in directory
        files.append(file)
print(files)

with open("thekey.key", "rb") as key: #read thekey.key
    secretkey = key.read()

secretphrase = "domz"

user_phrase = input("Enter the secret phrase tp decypt\n")

if user_phrase == secretphrase:
    for file in files: # loop for every files
        with open(file, "rb") as thefile: # read contents of all files
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents) # put the key to be a key of all files
        with open(file, "wb") as thefile: # let's decypt!
            thefile.write(contents_decrypted)
        print("congrate ! your file is unlock!")
else:
    print("It's wrong secret, fuck u !")