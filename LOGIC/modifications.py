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

def organize_files_by_category(folder_path,file_paths) :

    for file in file_paths :
        category = get_category(file)
        new_location = os.path.join(folder_path, category)

        if not os.path.exists(new_location) :
            os.makedirs(new_location)

        file_name = os.path.basename(file)
        current_location = file  # file is originally is a path of that file ,address
        destination = os.path.join(new_location, file_name)

        shutil.move(current_location, destination)





