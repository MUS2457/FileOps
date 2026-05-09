# FILEOPS – FILE MANAGEMENT CLI

FileOps is a lightweight command‑line tool I built to manage, organize, search, and analyze files inside any folder.  
It focuses on practical operations, clean architecture, and a smooth workflow.  
The tool scans all subfolders, builds a file list, and refreshes it after every action so the data is always up‑to‑date.

This project was fun to build — a mix of challenge, curiosity, and “let’s see how far I can push this”.

---

### OPERATIONS
- Organize files by category (images, videos, documents, audio, etc.)
- Delete files by name (with interactive selection)
- Find and delete duplicate files (hash‑based, chunk reading)
- Rename files (safe rename with confirmation)
- Move files to a new folder
- Delete empty folders (recursive)

### SEARCH
- Search files by name
- Search files by size range (MB)
- Full file age report (today, last 7 days, last 30 days, this year, older)
- Search files by extension

### ANALYSIS
- Count files by type (images, videos, documents…)
- Count files by extension
- Total size per type (MB)
- Largest and smallest file per type
- Global largest and smallest file
- Sort files by size per type
- Detect possible duplicates by size

---

## How It Works

1. The user enters a folder path.  
2. FileOps scans all subfolders and collects every file path.  
3. A menu appears with all available operations.  
4. After each action, FileOps rescans the folder so the next operation always uses fresh data.

Everything is built using Python’s standard modules — no external dependencies.


### Folder Roles

- **DATA/**  
  Handles scanning folders and defining file types/extensions.

- **OPERATIONS/**  
  All file modification actions:  
  - organize  
  - delete  
  - rename  
  - move  
  - delete empty folders  

- **LOGIC/**  
  Analysis logic:  
  - grouping  
  - counting  
  - size reports  
  - global max/min  
  - sorting  
  - possible duplicates  

- **UTILS/**  
  Helper functions:  
  - hashing  
  - search tools  
  - age report  
  - duplicate detection  

- **main.py**  
  The CLI entry point — handles user interaction and menu flow.

This architecture is clean, modular, and easy to extend — exactly how I like my backend tools.

---

## Purpose

FileOps was born from a simple truth:
every laptop I touch eventually becomes a chaotic mess.  
This tool is my way of breaking that curse.

Along the way, it became a great playground to practice:

- clean architecture

- modular design

- recursion

- hashing

- file system operations

- real‑time state tracking

- CLI user experience

## Future Improvements (Optional)
 
- Add ZIP archive tool  


