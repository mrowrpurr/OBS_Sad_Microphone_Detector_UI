# Application must be created before importing any other modules
from obs_mic_mute_detector.app import App
from obs_mic_mute_detector.system_tray import SystemTrayIcon

app = App()
###################

# pylint: disable=wrong-import-position,ungrouped-imports
from qt_helpers.run_app import run_app


def main():
    system_tray_icon = SystemTrayIcon(app)
    system_tray_icon.show()
    run_app(app)


if __name__ == "__main__":
    main()
