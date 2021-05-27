from __future__ import annotations
from typing import Mapping, Any, TypeVar
from enum import Enum
from abc import ABC, abstractmethod
import platform
from arc.color import fg, effects

from ..config import Config

T = TypeVar("T")


class OpenContext(Enum):
    DEFAULT = "Default"
    QUICK_LAUNCH = "QuickLaunch"


Items = Mapping[str, T]


class UIError(Exception):
    ...


class UIProvider(ABC):
    platform: str

    def __init__(self, items: Items, config: Config):
        self.items = items
        self.config = config
        self._display_items = self.format_items(items)

        if platform.system().lower() != self.platform.lower():
            raise UIError(
                f"{self.__class__.__name__} UI is only supported on {fg.YELLOW}{self.platform}{effects.CLEAR}"
            )

    @abstractmethod
    def run(self) -> T | None:
        """Run the UI Interface. Return the selected value"""

    def format_items(self, items: Items) -> Mapping[str, str]:
        """Format the input items"""
        return {key: key for key in items}

    def parse_output(self, output: Any) -> str:
        """Called post-execution, used to do any
        nessecary parsing of the chosen answer

        If no parsing is nessecary, there is no need
        to implement this method
        """
        return output
