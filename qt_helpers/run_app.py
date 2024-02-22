import asyncio

import qasync  # type: ignore [import-untyped]
from PySide6.QtWidgets import QApplication

app_close_event = asyncio.Event()


def run_app(app: QApplication) -> None:
    app.aboutToQuit.connect(slot=app_close_event.set)
    event_loop = qasync.QEventLoop(app)
    asyncio.set_event_loop(event_loop)
    with event_loop:
        event_loop.run_until_complete(app_close_event.wait())
