import os

def scan_folder_subfolders(path_folder):
    files_paths = []

    try:
        for item in os.listdir(path_folder):
            item_path = os.path.join(path_folder, item)

            if os.path.isfile(item_path):
                files_paths.append(item_path)

            elif os.path.isdir(item_path):
                sub_files = scan_folder_subfolders(item_path)
                files_paths.extend(sub_files)

    except PermissionError:
        # skip folders,files we can't access
        pass

    return files_paths