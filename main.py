import os

from LOGIC import analyser
from LOGIC import modifications
from LOGIC import tools


def main():
    print("=== FILE MANAGEMENT CLI ===")

    folder = input("Enter folder path: ").strip()

    if not os.path.exists(folder):
        print("Invalid path.")
        return

    file_paths = analyser.scan_folder_subfolders(folder)

    while True:
        print("\n=== MENU ===")

        # --- OPERATIONS ---
        print("\n[OPERATIONS]")
        print("1. Organize files by category")
        print("2. Delete file by name")
        print("3. Find & delete duplicates")
        print("4. Rename file")
        print("5. Move file")
        print("6. Delete empty folders")

        # --- SEARCH ---
        print("\n[SEARCH]")
        print("7. Search by name")
        print("8. Search by size range")
        print("9. File age report")

        # --- ANALYSER ---
        print("\n[ANALYSIS]")
        print("10. Count files by type")
        print("11. Count files by extension")
        print("12. Total size per type")
        print("13. Largest & smallest file per type")
        print("14. Global largest & smallest file")
        print("15. Sort files by size per type")
        print("16. Count files per size")
        print("17. Duplicate files")

        print("\n0. Exit")

        choice = input("\nChoose an option: ").strip()

        # ---------------- OPERATIONS ----------------

        if choice == "1":
            modifications.organize_files_by_category(folder, file_paths)

        elif choice == "2":
            modifications.delete_file_by_name(file_paths)

        elif choice == "3":
            duplicates = tools.find_duplicates(file_paths)
            modifications.delete_duplicate_files(duplicates)

        elif choice == "4":
            modifications.rename_file(file_paths)

        elif choice == "5":
            modifications.move_file(file_paths)

        elif choice == "6":
            modifications.delete_empty_folders(folder)

        # search tools

        elif choice == "7":
            (tools.search_by_name(file_paths))

        elif choice == "8":
            tools.search_by_size_range(file_paths)

        elif choice == "9":
            tools.full_age_report(file_paths)

        # analysis fc

        elif choice == "10":
            result = analyser.count_by_type(file_paths)
            print("\nFiles per type:")
            for k, v in result.items():
                print(f"{k}: {v}")

        elif choice == "11":
            result = analyser.count_by_extension(file_paths)
            print("\nFiles per extension:")
            for ext, data in result.items():
                print(f"{ext} ({data['types']}): {data['extensions_counter']}")

        elif choice == "12":
            result = analyser.tl_size_per_type(file_paths)
            print("\nTotal size per type (MB):")
            for k, v in result.items():
                print(f"{k}: {v} MB")

        elif choice == "13":
            result = analyser.get_max_min_size(file_paths)
            print("\nLargest & smallest per type:")
            for k, v in result.items():
                largest, l_size = v["largest"]
                smallest, s_size = v["smallest"]

                print(f"\n{k}:")
                print(f"  Largest: {largest} ({l_size} MB)")
                print(f"  Smallest: {smallest} ({s_size} MB)")

        elif choice == "14":
            result = analyser.global_max_min_file(file_paths)
            if result:
                largest, l_size = result["largest"]
                smallest, s_size = result["smallest"]

                print("\nGlobal files:")
                print(f"Largest: {largest} ({round(l_size / (1024**2), 2)} MB)")
                print(f"Smallest: {smallest} ({round(s_size / (1024**2), 2)} MB)")

        elif choice == "15":
            result = analyser.sort_files_by_size_type(file_paths)
            print("\nSorted files by type:")
            for k, files in result.items():
                print(f"\n{k}:")
                for file, size in files:
                    print(f"{file} - {round(size / (1024**2), 2)} MB")

        elif choice == "16":
            result = analyser.count_files_per_size(file_paths)
            print("\nFiles per size:")
            for size, count in result.items():
                print(f"{round(size / (1024**2), 2)} MB: {count} file(s)")

        elif choice == "17":
            duplicates = tools.find_duplicates(file_paths)
            for hashed, files in duplicates.items():
                print(f"{hashed}: {len(files)} file(s)")
                for file in files:
                    print(f"- {file}")


        elif choice == "0":
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")

        # track in real time the changes
        file_paths = analyser.scan_folder_subfolders(folder)


if __name__ == "__main__":
    main()