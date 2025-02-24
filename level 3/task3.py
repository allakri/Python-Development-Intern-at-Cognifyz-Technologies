import os
import time
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, List

class FileOrganizer:
    def __init__(self, watch_dir: str = "watch_folder"):
        self.watch_dir = watch_dir
        self.organized_dir = "organized_files"
        self.categories = {
            'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
            'documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.csv'],
            'audio': ['.mp3', '.wav', '.flac'],
            'video': ['.mp4', '.avi', '.mkv'],
            'archives': ['.zip', '.rar', '.7z']
        }
        self.setup_directories()
        
    def setup_directories(self) -> None:
        """Create necessary directories if they don't exist."""
        # Create watch directory
        Path(self.watch_dir).mkdir(exist_ok=True)
        
        # Create organized files directory
        Path(self.organized_dir).mkdir(exist_ok=True)
        
        # Create category subdirectories
        for category in self.categories:
            Path(f"{self.organized_dir}/{category}").mkdir(exist_ok=True)

    def get_category(self, file_extension: str) -> str:
        """Determine the category of a file based on its extension."""
        for category, extensions in self.categories.items():
            if file_extension.lower() in extensions:
                return category
        return 'others'

    def organize_files(self) -> Dict[str, List[str]]:
        """Organize files from watch directory into appropriate categories."""
        moved_files = {category: [] for category in self.categories.keys()}
        moved_files['others'] = []

        for file_path in Path(self.watch_dir).glob('*'):
            if file_path.is_file():
                extension = file_path.suffix
                category = self.get_category(extension)
                
                # Create destination path
                dest_dir = Path(f"{self.organized_dir}/{category}")
                dest_dir.mkdir(exist_ok=True)
                
                # Move file to appropriate directory
                try:
                    shutil.move(str(file_path), str(dest_dir / file_path.name))
                    moved_files[category].append(file_path.name)
                except Exception as e:
                    print(f"Error moving {file_path.name}: {e}")

        return moved_files

    def generate_report(self, moved_files: Dict[str, List[str]]) -> str:
        """Generate a report of the organized files."""
        report = f"File Organization Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        report += "=" * 50 + "\n\n"

        total_files = sum(len(files) for files in moved_files.values())
        report += f"Total files processed: {total_files}\n\n"

        for category, files in moved_files.items():
            if files:
                report += f"{category.capitalize()} ({len(files)} files):\n"
                for file in files:
                    report += f"  - {file}\n"
                report += "\n"

        report_path = f"organization_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(report_path, 'w') as f:
            f.write(report)

        return report_path

    def monitor_directory(self, interval: int = 5) -> None:
        """Monitor the watch directory for changes and organize files periodically."""
        print(f"Monitoring directory: {self.watch_dir}")
        print(f"Files will be organized every {interval} seconds")
        print("Press Ctrl+C to stop monitoring")
        
        try:
            while True:
                moved_files = self.organize_files()
                total_moved = sum(len(files) for files in moved_files.values())
                
                if total_moved > 0:
                    report_path = self.generate_report(moved_files)
                    print(f"\nOrganized {total_moved} files. Report generated: {report_path}")
                
                time.sleep(interval)
                
        except KeyboardInterrupt:
            print("\nMonitoring stopped by user")

def main():
    # Create and start the file organizer
    organizer = FileOrganizer()
    
    # Create some example files for demonstration
    demo_dir = Path(organizer.watch_dir)
    demo_files = [
        ('example.txt', 'This is a test file.'),
        ('document.pdf', 'PDF content'),
        ('image.jpg', 'Image content')
    ]
    
    print("Creating example files for demonstration...")
    for filename, content in demo_files:
        with open(demo_dir / filename, 'w') as f:
            f.write(content)
    
    # Start monitoring
    organizer.monitor_directory()

if __name__ == "__main__":
    main()