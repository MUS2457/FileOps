import os
from LOGIC import extension
import shutil


def get_category(file) :

    file_name = os.path.basename(file)
    _, ext = os.path.splitext(file_name)
    ext = ext.lower()

    for types , extensions in extension.extensions_by_type.items():

        if ext in extensions:
            return types

    return "other"

def get_safe_destination(category_folder, file_name):
    base, ext = os.path.splitext(file_name)
    destination = os.path.join(category_folder, file_name)
    counter = 1

    while os.path.exists(destination):  # Keep generating new names until a free one is found
        destination = os.path.join(category_folder, f"{base}_copy{counter}{ext}") # counter starts at 1, so first duplicate becomes _copy1
        counter += 1

    return destination


def organize_files_by_category(folder_path, file_paths):

    for file in file_paths:
        category = get_category(file)
        new_location = os.path.join(folder_path, category)

        if not os.path.exists(new_location):
            os.makedirs(new_location)

        file_name = os.path.basename(file)
        current_location = file

        destination = get_safe_destination(new_location, file_name)

        shutil.move(current_location, destination)


def delete_file_by_name(file_paths):
    while True:
        user = input("Enter the name of the file you would like to delete or 'exit' to quit: ").strip()

        if user.lower() == "exit":
            print("Exiting...")
            break

        if not user:
            print("Please enter a name")
            continue

        result = []

        for file in file_paths:
            file_name = os.path.basename(file)
            name, ext = os.path.splitext(file_name)

            if user.lower() == name.lower() or name.lower().startswith(user.lower()):
                result.append(file)

        if not result:
            print("No file found")
            continue

        dic = {}
        counter = 1
        for file in result:   # it s better if used,  for i, file in enumerate(result, start=1):  faster
            dic[counter] = file
            counter += 1

        print("\nFound files:")
        for key in dic:
            print(f"{key}: {os.path.basename(dic[key])}")

        while True:
            choice = input("Enter the number of the file you want to delete or 'back' to search: ").strip().lower()

            if choice == "back":
                print("Returning to search...")
                break

            if not choice:
                print("Please enter a number")
                continue

            try:
                choice = int(choice)
                if choice not in dic:
                    print("Invalid number")
                    continue
                break
            except ValueError:
                print("Please enter a valid number")

        if choice == "back":   # handle back before delete logic
            continue

        selected_file = dic[choice]
        file_name = os.path.basename(selected_file)

        confirm = input(f"Do you really want to delete {file_name}? [y/n] ").lower()

        if confirm == "y":
            os.remove(selected_file)
            print(f"Deleted {file_name}")
        else:
            print("Skipped.")


def delete_duplicate_files(duplicate):
    if not duplicate:
        print("No duplicate files found")
        return

    while True:
        print("\n=== DUPLICATE GROUPS ===")
        hash_map = {}
        # fun fact a dic it one tuple with 2 items per iteration: (key, value)
        # (hashed, files) unpack into 2 variables
        for i, (hashed, files) in enumerate(duplicate.items(), start=1):  # (i) represent the number of hash

            print(f"{i}. {hashed}  ({len(files)} files)")
            names = []

            for file in files:
                file_name = os.path.basename(file)
                names.append(os.path.basename(file_name))
            print(f"Files names : {names}")

            hash_map[i] = hashed  # store mapping for user selection

        user = input("\nEnter group number (or 'exit'): ").strip().lower()

        if user == "exit":
            print("Exiting...")
            break

        if not user.isdigit():
            print("Please enter a valid number")
            continue

        user = int(user)
        if user not in hash_map:
            print("Invalid group number")
            continue

        selected_hash = hash_map[user]
        files = duplicate[selected_hash]

        print(f"\n=== FILES IN GROUP: {selected_hash} ===")

        file_map = {i: f for i, f in enumerate(files, start=1)}

        for num, file_path in file_map.items():
            print(f"{num}. {os.path.basename(file_path)}")

        while True:
            user_2 = input("\nEnter file number to delete ('back' to return): ").strip().lower()

            if user_2 == "back":
                print("Returning to group selection...")
                break

            if not user_2.isdigit():
                print("Please enter a valid number")
                continue

            user_2 = int(user_2)
            if user_2 not in file_map:
                print("Invalid file number")
                continue

            selected_file = file_map[user_2]
            file_name = os.path.basename(selected_file)

            confirm = input(f"Delete {file_name}? (y/n/back): ").strip().lower()

            if confirm == "y":
                os.remove(selected_file)
                print(f"Deleted {file_name}")
                break

            elif confirm == "n":
                print("Skipped.")
                break

            elif confirm == "back":
                print("Returning to file list...")
                continue

            else:
                print("Please enter y, n, or back")
                continue

def rename_file(file_path):
    if not file_path:
        print("No file found")
        return

    while True:
        user = input("Enter file name to search (or 'exit'): ").strip().lower()

        if user == "exit":
            print("Exiting...")
            break

        if not user:
            print("Please enter a name")
            continue

        result = []
        for file in file_path:
            file_name = os.path.basename(file)
            if user in file_name.lower():
                result.append(file)

        if not result:
            print("No file found")
            continue

        file_map = {i: f for i, f in enumerate(result, start=1)}

        while True:
            print("\nMatched files:")
            for i, f in file_map.items():
                print(f"{i}. {os.path.basename(f)}")

            user_2 = input("\nEnter file number to rename ('back' to search): ").strip().lower()

            if user_2 == "back":
                print("Returning to search selection...")
                break

            if not user_2.isdigit() or int(user_2) not in file_map:
                print("Invalid number")
                continue

            chosen_file = file_map[int(user_2)]

            current_path = chosen_file
            folder = os.path.dirname(chosen_file)
            old_name = os.path.basename(chosen_file)
            name, ext = os.path.splitext(old_name)

            user_3 = input("Enter new name (without extension): ").strip()

            if not user_3:
                print("Invalid name")
                continue

            confirm = input("Confirm rename? [y/n]: ").strip().lower()
            if confirm != "y":
                print("Cancelled")
                continue

            new_name = user_3 + ext
            new_path = os.path.join(folder, user_3 + ext)
            os.rename(current_path, new_path)

            print(f"Renamed {old_name} → {new_name}")

def move_file(file_path):
    if not file_path:
        print("No file found")
        return

    while True:
        user = input("Enter the name of file you would like to move, 'exit' to quit ").strip().lower()

        if user == "exit" :
            print("Exiting...")
            break

        elif not user:
            print("Please enter a name")
            continue

        result = []

        for file in file_path:
            file_name = os.path.basename(file)
            if user in file_name.lower() or file_name.lower().startswith(user.lower()):
                result.append(file)

        if not result:
            print("No file found")
            continue

        file_map = {i: f for i, f in enumerate(result, start=1)}

        while True:
            print("\nMatched files:")
            for i, f in file_map.items():
                print(f"{i}. {os.path.basename(f)}")

            user_2 = input("\nEnter file number to move ('back' to search): ").strip().lower()

            if user_2 == "back":
                print("Returning to search selection...")
                break

            elif not user_2 or not user_2.isdigit() or int(user_2) not in file_map:
                print("Please enter a valid number")
                continue

            chosen_file = file_map[int(user_2)]
            folder = os.path.dirname(chosen_file)

            user_3 = input("Enter the name of folder you want the chosen file to move to it ").strip()

            destination = os.path.join(folder, user_3)

            confirm = input("Confirm move? [y] if not type anything else : ").strip().lower()

            if confirm == "y":

                if not os.path.exists(destination):
                    os.makedirs(destination)
                    shutil.move(chosen_file, destination)
                    print(f"Moved {chosen_file} to {destination}")

                else :
                    shutil.move(chosen_file, destination)
                    print(f"Moved {chosen_file} to {destination}")

                break

            else:
                print("Cancelled, returning to file selection...")
                continue

def delete_empty_folders(folder_path):
    deleted = []

    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item)

        # If it's a folder, clean inside it first
        if os.path.isdir(full_path):
            sub_deleted = delete_empty_folders(full_path)
            deleted.extend(sub_deleted)

            # After cleaning subfolders, check if this folder is now empty
            if not os.listdir(full_path):
                os.rmdir(full_path)
                deleted.append(full_path)
                print(f"Deleted: {full_path}")

    return deleted




















