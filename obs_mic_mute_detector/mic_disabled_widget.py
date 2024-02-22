from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

warning_image = QPixmap(":/WarningImage.png")
warning_image = warning_image.scaled(400, 400)


class MicDisabledWidget(QWidget):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

        self._layout = QVBoxLayout(self)
        self.setLayout(self._layout)

        title_label = QLabel("Mic is muted in OBS!")
        title_label.setStyleSheet("font-size: 40px; font-weight: bold;")
        self._layout.addWidget(title_label)

        image_label = QLabel()
        image_label.setPixmap(warning_image)
        self._layout.addWidget(image_label)

        self.resize(400, 400)

    def closeEvent(self, event):
        event.ignore()
        self.hide()
