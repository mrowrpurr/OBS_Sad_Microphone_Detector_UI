import os

from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QWidget
from watchdog.events import FileSystemEventHandler


class LogFileHandler(FileSystemEventHandler):
    def __init__(
        self,
        folder_path: str,
        app: QApplication,
        icon: QSystemTrayIcon,
        warning_popup_widget: QWidget,
    ):
        self.folder_path = folder_path
        self.last_modified_file = None
        self.app = app
        self.icon = icon
        self.warning_popup_widget = warning_popup_widget

    def on_modified(self, event):
        # Check if it's a .txt file
        if event.is_directory or not event.src_path.endswith(".txt"):
            return

        # Update the last modified file details
        if (
            not self.last_modified_file
            or event.src_path != self.last_modified_file["path"]
        ):
            self.last_modified_file = {
                "path": event.src_path,
                "mtime": os.path.getmtime(event.src_path),
            }

        # Tail the last modified file for the specific text
        self.check_file_for_text(event.src_path)

    def check_file_for_text(self, file_path: str):
        print(f"Checking {file_path}")
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                if "invalidated" in line:
                    print("Mic is muted in OBS!")
                    self.warning_popup_widget.show()
                    break
