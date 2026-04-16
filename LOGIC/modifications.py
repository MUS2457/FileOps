import os
from LOGIC import extension
from LOGIC.analyser import scan_folder_subfolders
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

        elif not user:
            print("Please enter a name")
            continue

        found = False
        result = []
        dic = {}
        counter = 1

        for file in file_paths:
            file_name = os.path.basename(file)
            name, ext = os.path.splitext(file_name)

            if user.lower() == name.lower():
                result.append(file)
                found = True

                for item in result:
                   dic[counter] = item
                   counter += 1

                for key, value in dic.items():
                    print(f"{key}: {value}")

                user_2 = input("Enter one of the files based on the number ").strip()
                if not user
                confirm = input(f"Do you really want to delete {file_name}? [y/n] ").lower()

                if confirm == "y":
                    os.remove(file)
                    print(f"Deleted {file_name}")
                elif confirm == "n":
                    print("Skipped.")

        if not found:
            print("No file found with the given name.")









