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
        self.exec: str = kwargs.get("exec", self.default["exec"])
        self.show_icons: bool = kwargs.get("show_icons", self.default["show_icons"])
        self.show_hidden: bool = kwargs.get("show_hidden", self.default["show_hidden"])
        self.show_files: bool = kwargs.get("show_files", self.default["show_files"])
        self.ui_provider: str = kwargs.get("ui_provider", self.default["ui_provider"])
        self.wofi: Dict[str, str] = kwargs.get("wofi", self.default["wofi"])
        self.rofi: Dict[str, str] = kwargs.get("rofi", self.default["rofi"])

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
