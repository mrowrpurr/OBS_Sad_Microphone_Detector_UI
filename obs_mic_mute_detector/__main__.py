#################################################################
# Application must be created before importing any other modules
from obs_mic_mute_detector.app import App
from obs_mic_mute_detector.mic_levels_detector import monitor_microphone
from obs_mic_mute_detector.qrc_resources import qt_resource_data  # noqa: F401q

app = App()
#################################################################

# pylint: disable=wrong-import-position,ungrouped-imports,wrong-import-order


from obs_mic_mute_detector.mic_disabled_widget import MicDisabledWidget
from obs_mic_mute_detector.system_tray import SystemTrayIcon
from qt_helpers.run_app import run_app

QRC_RESOURCES = qt_resource_data

warning_popup_widget = MicDisabledWidget()


def show_warning_popup() -> None:
    warning_popup_widget.show()


def main():
    # folder_to_watch = "C:/Users/mrowr/AppData/Roaming/obs-studio/logs"

    show_warning_popup()

    monitor_microphone(None, show_warning_popup)

    system_tray_icon = SystemTrayIcon(app)
    system_tray_icon.show()

    # event_handler = LogFileHandler(
    #     folder_to_watch, app, system_tray_icon, warning_popup_widget
    # )
    # observer = Observer()
    # observer.schedule(event_handler, folder_to_watch, recursive=False)
    # observer_thread = Thread(target=observer.start, daemon=True)
    # observer_thread.start()

    run_app(app)


if __name__ == "__main__":
    main()
