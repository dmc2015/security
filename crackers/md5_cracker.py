from os.path import isfile, join
import random
from os import listdir
import hashlib
import pdb

hashed_password_lists = list(open('generated_hashes.txt', 'r'))
random_selected_hash = random.choice(hashed_password_lists)


password_lists = [f for f in listdir('./password_lists') if isfile(join('./password_lists', f))]


for item in password_lists:
    password_list_file = open("password_lists/" + item, "r")
    for word in password_list_file.readlines():
        word = word.strip("\n")
        hashed_pw = hashlib.md5(word.encode('utf-8'))

        if hashed_pw.hexdigest() == random_selected_hash.strip("\n"):
            print("Cracked : " + word)
    
