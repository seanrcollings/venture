from typing import Dict
import os
import yaml

from .types import DirectorySchema
from . import util


class Config:
    default = {
        "directories": ["~"],
        "exec": "code -r",
        "ui_provider": "rofi",
        "show_icons": True,
        "show_hidden": False,
        "show_files": True,
        "wofi": {},
        "rofi": {},
    }

    def __init__(self, **kwargs):

        self.directories: DirectorySchema = kwargs.get(
            "directories", self.default["directories"]
        )
        self.exec: str = kwargs.get("exec") or self.default["exec"]  # type: ignore
        self.show_icons: bool = kwargs.get("show_icons") or self.default["show_icons"]  # type: ignore
        self.show_hidden: bool = (
            kwargs.get("show_hidden") or self.default["show_hidden"]  # type: ignore
        )
        self.show_files: bool = kwargs.get("show_files") or self.default["show_files"]  # type: ignore
        self.ui_provider: str = kwargs.get("ui_provider") or self.default["ui_provider"]  # type: ignore
        self.wofi: Dict[str, str] = kwargs.get("wofi") or self.default["wofi"]  # type: ignore
        self.rofi: Dict[str, str] = kwargs.get("rofi") or self.default["rofi"]  # type: ignore

    @classmethod
    def dump_default(cls):
        return yaml.dump(cls.default, Dumper=yaml.Dumper)


config_path = util.resolve("~/.config/venture.yaml")
if os.path.isfile(config_path):
    file = open(config_path)
    contents = file.read()
    file.close()
    config = Config(**yaml.load(contents, Loader=yaml.Loader))
else:
    config = Config()
