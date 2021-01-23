from .ui_provider import UIProvider
from ..util import resolve


class Wofi(UIProvider):
    command = "wofi"

    def get_commandline_args(self, config):
        args = ["--dmenu"]
        if conf := config.wofi.get("config"):
            args.append("--conf")
            args.append(resolve(conf))
        if style := config.wofi.get("stylesheet"):
            args.append("--style")
            args.append(resolve(style))

        return args

    def parse_output(self, output: bytes):
        choice = output.decode("utf-8").strip("\n")
        return choice
