import hashlib
from os import listdir
import pdb
from os.path import isfile, join


password_lists = [f for f in listdir('./password_lists') if isfile(join('./password_lists', f))]
file = open('generated_hashes.txt', 'w')

for item in password_lists:
    password_list_file = open("password_lists/" + item, "r")
    for word in password_list_file.readlines():
        word = word.strip("\n")
        hashed_pw = hashlib.md5(word.encode('utf-8'))
        file.write(hashed_pw.hexdigest() + "\n")
file.close()