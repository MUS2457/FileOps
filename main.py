from LOGIC.analyser import scan_folder_subfolders
from LOGIC.modifications import delete_file_by_name

def main():
    user = input("Username: ")
    files_path = scan_folder_subfolders(user)
    delete_file_by_name(files_path)

if __name__ == "__main__":
    main()