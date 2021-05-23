from .ui_provider import UIProvider
from ..util import resolve


class Rofi(UIProvider):
    command = "rofi"

    def get_commandline_args(self, config):
        args = ["-dmenu"]
        if theme := config.rofi.get("theme"):
            args.append("-theme")
            args.append(resolve(theme))

        return args

    def parse_output(self, output: bytes):
        choice = output.decode("utf-8").strip("\n")
        return choice
