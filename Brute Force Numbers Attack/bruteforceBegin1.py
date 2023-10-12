import random
import hashlib

wanted_hash = "3cc6520a6890b92fb55a6b3d657fd1f6"

def convert_str_to_hash(str):
    hash_str = hashlib.md5(str.encode('utf-8')).hexdigest()
    return hash_str





for i in range(99999, 1000000):
    test_hash = convert_str_to_hash(str(i))
    if test_hash == wanted_hash:
        print("The password is: " + str(i))
        exit()
    else:
        print("The password is not: " + str(i))
        print()

