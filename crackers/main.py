import crypt
import pdb
from os import walk
from os import listdir
from os.path import isfile, join
import hashlib

# pdb.set_trace()
password_lists = [f for f in listdir('./password_lists') if isfile(join('./password_lists', f))]
salt = ""
pw = ""
list_count = 0

for item in password_lists:
    file = open("password_lists/" + item, "r")
    print("Trying...")
    print("List Number: " + str(list_count))
    print("List Name: " + item)
    list_count += 1

    for word in file.readlines():
        word = word.strip("\n")
        hash = crypt.crypt(word, salt)
        target_hash = hashlib.md5(''.encode())
        
        if hash == pw:
            print("password found")
            print(word)
            break