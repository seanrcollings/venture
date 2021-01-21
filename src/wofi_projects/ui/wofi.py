from typing import cast, Dict


from .ui_provider import UIProvider


class Wofi(UIProvider):
    command = "wofi"

    def get_commandline_args(self, config):
        args = ["--dmenu"]
        wofi_conf = cast(Dict[str, str], config.wofi)
        if conf := wofi_conf.get("config"):
            args.append("--conf")
            args.append(conf)
        if style := wofi_conf.get("stylesheet"):
            args.append("--style")
            args.append(style)

        return args

    def parse_output(self, output: bytes):
        choice = output.decode("utf-8").strip("\n")
        return choice
