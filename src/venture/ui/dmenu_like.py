from typing import Iterable, Type
import subprocess
from .ui_provider import UIProvider

from ..config import Config


class DmenuLike(UIProvider):
    default_args: list[str] = []
    argument_format: str

    def run(self, projects, config) -> str:
        args = self.get_commandline_args(config)
        output = self.execute(projects, args)
        return self.parse_output(output)

    def get_commandline_args(self, config: Config) -> Iterable[str]:
        configuration: dict = config[self.command]
        return [self.format_arg(name, value) for name, value in configuration.items()]

    def format_arg(self, name, value):
        return self.argument_format.format(name=name, value=value)

    def execute(self, projects: list[str], args):
        """Execute the UI command.

        This implementation expects the UI to be an external process
        and for it to recieve it's input as a newline-seperated
        list of strings from stdin.
        """
        breakpoint()
        proc = subprocess.Popen(
            [self.command, *self.default_args, *args],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
        )
        return proc.communicate(bytes("\n".join(projects), "utf-8"))[0]

    def parse_output(self, output: bytes):
        choice = output.decode("utf-8").strip("\n")
        return choice


class Dmenu(DmenuLike):
    command = "dmenu"
    argument_format = "--{name} {value}"


class Rofi(DmenuLike):
    command = "rofi"
    default_args = ["-dmenu"]
    argument_format = "-{name} {value}"


class Wofi(DmenuLike):
    command = "wofi"
    default_args = ["--dmenu"]
    argument_format = "--{name} {value}"

    alias_map = {"stylesheet": "style", "config": "conf"}

    def format_arg(self, name, value):
        if name in self.alias_map:
            name = self.alias_map[name]
        super().format_arg(name, value)


dmenu_like_menus: dict[str, Type[DmenuLike]] = {
    "dmenu": Dmenu,
    "rofi": Rofi,
    "wofi": Wofi,
}