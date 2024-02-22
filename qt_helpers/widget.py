from dataclasses import dataclass
from typing import Callable, Type, TypeVar

from PySide6.QtWidgets import QBoxLayout, QWidget

T = TypeVar("T", bound=QWidget)


def widget(
    name: str | None = None,
    classes: list[str] | None = None,
    layout: QBoxLayout.Direction | None = None,
) -> Callable[[Type[T]], Type[T]]:
    def decorator(cls: Type[T]) -> Type[T]:
        # Ensure the class is treated as a dataclass
        def new_post_init(self: T) -> None:
            QWidget.__init__(self)  # pylint: disable=unnecessary-dunder-call

            # Setup widgets
            if hasattr(self, "_setup"):
                self._setup()  # pylint: disable=protected-access

            if hasattr(self, "_ids"):
                self._ids()  # pylint: disable=protected-access

            # Apply additional configurations
            if name:
                self.setObjectName(name)
            if classes:
                self.setProperty("class", f"|{'|'.join(classes)}|")
            if layout is not None:
                the_layout = QBoxLayout(layout)
                self.setLayout(the_layout)
                if hasattr(self, "_layout"):
                    self._layout(the_layout)  # pylint: disable=protected-access

        cls.__post_init__ = new_post_init  # type: ignore[attr-defined]
        cls = dataclass(cls)

        return cls

    return decorator
