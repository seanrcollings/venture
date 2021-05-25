from typing import Any
from abc import ABC, abstractmethod


class UIProvider(ABC):
    command: str = ""

    @abstractmethod
    def run(self, projects, config) -> str:
        """Run the UI Interface. Return the selected value"""

    def parse_output(self, output: Any) -> Any:
        """Called post-execution, used to do any
        nessecary parsing of the chosen answer

        If no parsing is nessecary, there is no need
        to implement this method
        """
        return output
