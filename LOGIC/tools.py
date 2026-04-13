from LOGIC import analyser
import os
import hashlib

def hash_file(file_path):
    hasher = hashlib.md5()  # create a hash object

    with open(file_path, "rb") as file:  # open the file in binary mode
        while True:
            chunk = file.read(4096) # read a small part of the file

            if not chunk:  # stop when there's no more data
                break
            hasher.update(chunk)  # add this part to the hash

    return hasher.hexdigest()

def find_duplicates(file_paths):
    possible_duplicates = analyser.possible_duplicates(file_paths)

    hash_groups = {}

    # Step 1: group files by hash
    for size, files in possible_duplicates.items():
        for file in files:
            file_hash = hash_file(file)

            if file_hash not in hash_groups:
                hash_groups[file_hash] = []

            hash_groups[file_hash].append(file)

    # Step 2: keep only real duplicates
    duplicates = {}

    for file_hash, files in hash_groups.items():
        if len(files) > 1:
            duplicates[file_hash] = files

    return duplicates







