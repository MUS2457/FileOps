FILEOPS – FILE MANAGEMENT CLI

FileOps is a simple command‑line tool for managing, organizing, searching, and analyzing files inside any folder. It focuses on practical operations and a clean workflow. The tool scans all subfolders, builds a file list, and updates it after every operation so the data is always fresh.

FEATURES

OPERATIONS

Organize files by category (images, videos, documents, audio, etc.)

Delete file by name

Find and delete duplicate files (hash based, chunk reading)

Rename files

Move files

Delete empty folders (recursive)

SEARCH

Search files by name

Search files by size range

Full file age report

Search files by extension

ANALYSIS

Count files by type

Count files by extension

Total size per type

Largest and smallest file per type

Global largest and smallest file

Sort files by size per type

Count files per size

Duplicate file report

HOW IT WORKS

The user enters a folder path.

FileOps scans all subfolders and collects every file path.

The menu appears with all available operations.

After each action, FileOps rescans the folder so the next operation always uses updated data.

No external libraries are required. Everything uses Python’s built‑in modules.

INSTALLATION

Run the project with:

python main.py

USAGE EXAMPLE

=== FileOps by RaijinCode Final version ===
Enter folder path: /Users/you/Desktop/Projects

=== MENU ===

Organize files by category

Delete file by name

Find and delete duplicates
...

Search by extension
...

Exit

Choose a number and FileOps performs the selected action.

PROJECT STRUCTURE

FileOps/
main.py
LOGIC/
analyser.py
modifications.py
tools.py
README.md

main.py handles the menu and user interaction.
analyser.py contains counting, sorting, and size analysis.
modifications.py contains rename, move, delete, and organize operations.
tools.py contains search tools, duplicate finder, and age report.

PURPOSE

FileOps was created to practice and demonstrate:

clean architecture

modular design

recursion

hashing

file system operations

real‑time state tracking

CLI user experience

It is both a practical tool and a structured learning project.

FUTURE IMPROVEMENTS (OPTIONAL)

Add logging

Add undo history

Add ZIP archive tool

Add configuration file for custom categories