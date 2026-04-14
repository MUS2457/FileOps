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
    # group files by hash
    for size, files in possible_duplicates.items():
        for file in files:
            file_hash = hash_file(file)

            if file_hash not in hash_groups:
                hash_groups[file_hash] = []

            hash_groups[file_hash].append(file)

    duplicates = {}

    for file_hash, files in hash_groups.items():
        if len(files) > 1:
            duplicates[file_hash] = files

    return duplicates

def search_by_name(file_paths):
    while True :
        user = input("Please enter name of the file you would like to search for ,"
                     "or 'exit' to quit: ").strip()

        if user == "exit":
            print("Exiting...")
            break
        elif not user:
            print("Please enter a valid file name.")
            continue

        results = []

        for file in file_paths:
            file_name = os.path.basename(file)
            name, _ = os.path.splitext(file_name)

            if user.lower() == name.lower() or name.lower().startswith(user.lower()):
                results.append(file)

        if results:
            print(f"Found {len(results)} file(s).")
            for file in results:
                print(f"- {file}")

            return results

        else:
            print("No file found.")


def search_by_size_range(file_paths):
    file_sized = analyser.group_files_by_size(file_paths)

    while True:
        try:
            user_1 = int(input("Please enter minimum size (MB): "))
            user_2 = int(input("Please enter maximum size (MB): "))

            if user_1 > user_2:
                print("The minimum range is bigger than the maximum range.")
                continue

            if user_1 < 0 or user_2 < 0:
                print("The range cannot be negative.")
                continue

            if user_2 == 0:
                print("No range provided.")
                continue

        except ValueError:
            print("Enter valid ranges.")
            continue

        min_bytes = user_1 * (1024 ** 2)  # convert to bytes to compare avoid weird error
        max_bytes = user_2 * (1024 ** 2)

        results = {}

        for size, files in file_sized.items():
            if min_bytes <= size <= max_bytes:
                results[size] = files[:]   # copy the list of files with same element

        if results:
            for size, files in results.items():
                size_mb = round(size / (1024 ** 2), 2)
                print(f"\nSize: {size_mb} MB")
                print(f"Files ({len(files)}):")
                for f in files:
                    print(f"- {f}")
            return results

        else:
            print("No files found in this range.")







