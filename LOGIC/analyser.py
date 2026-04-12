import os
from LOGIC.extension import extensions_by_type

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


def group_files_by_size(files_paths):
    sized_files = {}

    for file in files_paths:
        try:
            file_size = os.path.getsize(file)

            if file_size not in sized_files:
                sized_files[file_size] = []

            sized_files[file_size].append(file)

        except OSError:
            # Skip files that cant be accessed for ex : deleted ,permission
            continue

    return sized_files

def count_files_per_size(files_paths):
    sized_files = group_files_by_size(files_paths)
    sized_files_count = {}

    if not sized_files:
        return sized_files_count

    for size, files in sized_files.items():
        sized_files_count[size] = len(files)

    return sized_files_count


def group_files(files_paths):
    extension_group = {}

    for file in files_paths:
        name, extension = os.path.splitext(file)
        extension = extension.lower()

        found = False

        for types, extensions in extensions_by_type.items():
            if extension in extensions:
                if types not in extension_group:
                    extension_group[types] = []
                extension_group[types].append(file)
                found = True
                break

        if not found:
            types = "other"
            if types not in extension_group:
                extension_group[types] = []
            extension_group[types].append(file)

    return extension_group

def count_by_type(files_paths):
    type_counter = {}
    grouped = group_files(files_paths)

    if not grouped:
        return type_counter

    for types, files in grouped.items():
        type_counter[types] = len(files)

    return type_counter

def count_by_extension(files_paths):
    extension_counter = {}
    grouped = group_files(files_paths)

    if not grouped:
        return extension_counter

    for types, files in grouped.items():

        for file in files:
            filename = os.path.basename(file)
            name, extension = os.path.splitext(filename)
            extension = extension.lower()

            if extension not in extension_counter:
                extension_counter[extension] = {"types": types, "extensions_counter": 1}
            else:  #without else i should set the first count into 0 instead of 1
                extension_counter[extension]["extensions_counter"] += 1

    return extension_counter

def size_by_type(files_paths):
    size_counter = {}
    grouped = group_files(files_paths)

    if not grouped:
        return size_counter

    for types, files in grouped.items():
        total_size = 0

        for file in files:
            try:
                file_size = os.path.getsize(file)
                total_size += file_size
            except OSError:
                continue

        size_counter[types] = round(total_size / (1024 * 1024), 2)

    return size_counter
