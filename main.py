from LOGIC.analyser import scan_folder_subfolders
from LOGIC.modifications import organize_files_by_category

def main():
    user = input("Username: ")
    files_path = scan_folder_subfolders(user)
    organize_files_by_category(user, files_path)


if __name__ == "__main__":
    main()