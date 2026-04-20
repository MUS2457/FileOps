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
        user = input("Enter the name of file you want to rename it , or 'exit' to quit ").strip().lower()

        if user.lower() == "exit":
            print("Exiting...")
            break

        elif not user:
            print("Please enter a name")
            continue

        result = []

        for file in file_path:
            file_name = os.path.basename(file)

            if user.lower() == file_name.lower() or file_name.lower().startswith(user.lower()):
                result.append(file)

        if not result:
            print("No file found")
            continue

        file_map = {i: f for i, f in enumerate(result, start=1)}

        for i, file in file_map.items():
            print(f"{i}. {os.path.basename(file)}")
            while True:
               user_2 = input("\nEnter file number to rename ,('back') to comeback): ").strip().lower()

               if user_2.lower() == "back" :
                   print("Returning to file search")
                   break

               elif not user_2 or not user_2.isdigit():
                   print("Please enter a valid number")
                   continue

               user_2 = int(user_2)


               if user_2 not in file_map :
                   print("Invalid file number")
                   continue

               chosen_file = file_map[user_2]
               current_path = chosen_file
               path_only = os.path.dirname(current_path)
               file_name = os.path.basename(chosen_file)
               name,ext = os.path.splitext(file_name)


               user_3 = input("What would you like to rename?, or 'back' to search ").strip().lower()

               if user_3 == "back":
                    print("Returning to file choose menu")
                    continue


               confirm = input("Are you sure you want to rename? [y/n] ").strip().lower()

               if confirm == "n":
                   print("Renaming has been cancelled")
                   continue

               elif confirm == "y":
                   file_name2 = user_3 + ext
                   new_path = os.path.join(path_only, file_name2)
                   os.rename(chosen_file, new_path)
                   print(f"Renamed {file_name} to {file_name2}")













