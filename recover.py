from cryptography.fernet import Fernet
import os

def decrypt(files, key_file):
    with open(key_file, 'rb') as pandora:
        key = pandora.read()
    f = Fernet(key)

    for file in files:
        with open(file, 'rb') as encrypted_file:
            encrypted = encrypted_file.read()

        decrypted = f.decrypt(encrypted)
        new_file_name = file.replace(".pandora","")

        with open(new_file_name, 'wb') as decrypted_file:
            decrypted_file.write(decrypted)

        os.remove(file)

def os_walk(dir):
    file_list = []
    for cur_dir, _, files in os.walk(dir):
        for file in files:
            complete_path = os.path.join(cur_dir, file)
            file_list.append(complete_path)
    return file_list

key_file = str(input("Enter key file directory [Example: dir1/dir2/mykey.key]: "))
directory = str(input("Type the directory you want to save: "))

files = os_walk(directory)
decrypt(files, key_file)
