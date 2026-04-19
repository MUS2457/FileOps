from LOGIC.analyser import scan_folder_subfolders
from LOGIC import tools
from LOGIC import modifications

def main():
    user = input("Username: ")
    files_path = scan_folder_subfolders(user)
    duplicates_path = tools.find_duplicates(files_path)
    modifications.delete_duplicate_files(duplicates_path)


if __name__ == "__main__":
    main()