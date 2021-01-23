from typing import Dict
import os
import yaml

from .types import DirectorySchema
from . import util


class Config:
    default = {
        "directories": ["~"],
        "exec": "code -r",
        "ui_provider": "wofi",
        "show_icons": True,
        "show_hidden": False,
        "show_files": True,
        "wofi": {
            "config": "~/.config/wofi/projects/config",
            "stylesheet": "~/.config/wofi/projects/style.css",
        },
    }

    def __init__(self, **kwargs):

        self.directories: DirectorySchema = (
            kwargs.get("directories") or self.default["directories"]
        )
        self.exec: str = kwargs.get("exec") or self.default["exec"]
        self.show_icons: bool = kwargs.get("show_icons") or self.default["show_icons"]
        self.show_hidden: bool = (
            kwargs.get("show_hidden") or self.default["show_hidden"]
        )
        self.show_files: bool = kwargs.get("show_files") or self.default["show_files"]
        self.ui_provider: str = kwargs.get("ui_provider") or self.default["ui_provider"]
        self.wofi: Dict[str, str] = kwargs.get("wofi") or self.default["wofi"]

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
