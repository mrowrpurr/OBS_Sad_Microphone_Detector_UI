from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMenu, QSystemTrayIcon

ICON_PATH = ":/Icon.png"


class SystemTrayIcon(QSystemTrayIcon):
    def __init__(self, app: QApplication, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setIcon(QIcon(ICON_PATH))
        self.setToolTip("OBS Mic Mute Detector")
        self._create_menu(app)

    def _create_menu(self, app):
        menu = QMenu()
        exit_action = menu.addAction("Exit")
        exit_action.triggered.connect(app.quit)
        self.setContextMenu(menu)
