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
            else:  #without else I should set the first count into 0 instead of 1
                extension_counter[extension]["extensions_counter"] += 1

    return extension_counter

def tl_size_per_type(files_paths):
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

def get_files_size_per_type(files_paths):
    files_per_type = group_files(files_paths)
    files_type_size = {}

    if not files_per_type:
        return files_type_size

    for types, files in files_per_type.items():
        for file in files:
            try:
                file_size = os.path.getsize(file)
            except OSError:
                continue

            if types not in files_type_size:
                files_type_size[types] = {}

            files_type_size[types][file] = file_size

    return files_type_size

def get_max_min_size(files_paths):
    files_sizes_per_type = get_files_size_per_type(files_paths)
    large_small = {}

    if not files_sizes_per_type:
        return large_small

    for types, files in files_sizes_per_type.items():

        largest_file = max(files, key=files.get)
        smallest_file = min(files, key=files.get)

        large_small[types] = {
            "largest": (largest_file, round(files[largest_file] / (1024 * 1024), 2)),
            "smallest": (smallest_file, round(files[smallest_file] / (1024 * 1024), 2))
        }

    return large_small

def global_max_min_file(files_paths):
    all_files = {}

    if not files_paths:
        return all_files

    for file in files_paths:
        try:
            file_size = os.path.getsize(file)
        except OSError:
            continue

        all_files[file] = file_size

    global_max_file = max(all_files, key=all_files.get)
    global_min_file = min(all_files, key=all_files.get)

    return {
        "largest": (global_max_file, all_files[global_max_file]),
        "smallest": (global_min_file, all_files[global_min_file])
    }

def sort_files_by_size_type(files_paths):
    files_per_type = get_files_size_per_type(files_paths)
    sorted_files_per_type = {}
    if not files_per_type:
        return files_per_type

    for types, files in files_per_type.items():
        list_sort = sorted(files.items(), key= lambda item: item[1])  #item [1] refers to size
        sorted_files_per_type[types] = list_sort

    return sorted_files_per_type

def possible_duplicates(files_paths):
    files_sized = group_files_by_size(files_paths)
    possible_duplicate = {}

    if not files_sized:
        return possible_duplicate

    for size, files in files_sized.items():
        if len(files) > 1:
            possible_duplicate[size] = files

    return possible_duplicate