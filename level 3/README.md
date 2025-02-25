# File Organizer

## Overview
The **File Organizer** is a Python script that automatically organizes files in a specified directory based on their file extensions. It categorizes files into predefined folders and continuously monitors the directory for new files.

## Features
- 📂 **Automatic File Sorting**: Organizes files into categories such as Images, Documents, Audio, Video, Archives, and Others.
- 🔄 **Real-time Monitoring**: Watches the directory and moves files automatically at regular intervals.
- 📋 **Report Generation**: Creates a report summarizing organized files.
- 🚀 **Easy to Use & Extendable**: Add more file categories as needed.
- 🛡️ **Error Handling**: Handles exceptions when moving files.

---

## Directory Structure
```
project_folder/
  ├── task3.py  # Main script
  ├── watch_folder/      # Directory to be monitored (auto-created)
  ├── organized_files/   # Destination directory (auto-created)
      ├── images/
      ├── documents/
      ├── audio/
      ├── video/
      ├── archives/
      ├── others/
  ├── README.md          # Project documentation
```

---

## Installation & Setup
### Prerequisites
Ensure you have **Python 3.x** installed.

### Steps
1. **Clone or Download** the repository.
2. Open a terminal and navigate to the project folder.
3. Run the script:
   ```sh
   python task3.py
   ```

---

## How It Works
### Initialization
- The script creates a `watch_folder/` (if not already present) where files should be placed for sorting.
- It also creates an `organized_files/` folder with subdirectories for different file types.

### File Organization
- The script scans the `watch_folder/` and moves files to the appropriate category based on extensions.
- Unrecognized file types go into the `others/` folder.

### Monitoring Mode
- The script continuously monitors `watch_folder/` and organizes files every **5 seconds**.
- Press **Ctrl + C** to stop monitoring.

### Report Generation
- After organizing, a **report file** (`organization_report_YYYYMMDD_HHMMSS.txt`) is created, listing moved files.

---

## Supported File Categories
| Category    | File Extensions                                   |
|------------|-------------------------------------------------|
| Images     | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`        |
| Documents  | `.pdf`, `.doc`, `.docx`, `.txt`, `.xlsx`, `.csv` |
| Audio      | `.mp3`, `.wav`, `.flac`                        |
| Video      | `.mp4`, `.avi`, `.mkv`                         |
| Archives   | `.zip`, `.rar`, `.7z`                          |
| Others     | Any unrecognized file types                    |

---

## Example Output
```
Monitoring directory: watch_folder
Files will be organized every 5 seconds
Press Ctrl+C to stop monitoring

Organized 3 files. Report generated: organization_report_20250225_123456.txt
```

Example **Report File (`organization_report_YYYYMMDD_HHMMSS.txt`)**:
```
File Organization Report - 2025-02-25 12:34:56
==================================================

Total files processed: 3

Documents (1 files):
  - example.pdf

Images (1 files):
  - photo.jpg

Others (1 files):
  - unknown.xyz
```

---

## Customization
To add more file categories, modify the `self.categories` dictionary inside `FileOrganizer`:
```python
self.categories = {
    'images': ['.jpg', '.jpeg', '.png'],
    'scripts': ['.py', '.js', '.sh'],  # Added new category
    'others': []  # Catch-all for unknown types
}
```

---

## License
This project is open-source. Feel free to modify and use it for your needs.

---

## Author
Developed by **[raiAbhishek]**

