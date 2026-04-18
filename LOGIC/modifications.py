import os
from LOGIC import extension, analyser
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
        for file in result:
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
        return None
