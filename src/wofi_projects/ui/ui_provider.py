from typing import List, Any
from abc import ABC, abstractmethod
import subprocess

from ..config import Config


class UIProvider(ABC):
    @property
    @abstractmethod
    def command(self) -> str:
        """Command to execute"""

    def run(self, projects, config):
        args = self.get_commandline_args(config)
        output = self.execute(projects, args)
        return self.parse_output(output)

    @abstractmethod
    def get_commandline_args(self, config: Config) -> List[str]:
        """Get the args to add to command line execution

        :param config: instance of the app's Config

        :returns: a List of shell-acceptable strings
        """

    def execute(self, projects: List[str], args):
        """Execute the UI command.

        This implementation expects the UI to be an external process
        and for it to recieve it's input as a newline-seperated
        list of strings from stdin.
        """

        proc = subprocess.Popen(
            [self.command, *args],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
        )
        return proc.communicate(bytes("\n".join(projects), "utf-8"))[0]

    def parse_output(self, output: Any) -> str:
        """Called post-execution, used to do any
        nessecary parsing of the chosen answer

        If no parsing is nessecary, there is no need
        to implement this method
        """
        return output
