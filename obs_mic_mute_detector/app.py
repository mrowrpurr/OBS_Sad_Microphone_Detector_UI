from PySide6.QtWidgets import QApplication


class App(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setApplicationName("Quill")
        self.setApplicationDisplayName("Quill")
        self.setStyle("Fusion")
