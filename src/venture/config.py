from typing import Any
import os
import yaml

from .types import DirectorySchema, QuickLaunchSchema
from . import util


class Config:
    directories: DirectorySchema = ["~"]
    exec: str = "code -r {path}"
    ui_provider: str = "rofi"
    show_icons: bool = True
    show_hidden: bool = False
    show_files: bool = True
    include_parent_folder: bool = False
    wofi: dict[str, str] = {}
    rofi: dict[str, str] = {}
    dmenu: dict[str, str] = {}
    quicklaunch: QuickLaunchSchema = []

    def __getitem__(self, item):
        return getattr(self, item)

    def dict(self):
        yield from [
            (prop, getattr(self, prop))
            for prop in dir(self)
            if not prop.startswith("_") and not callable(getattr(self, prop))
        ]

    @classmethod
    def from_file(cls, file):
        file = open(file)
        contents = file.read()
        file.close()
        data: dict[str, Any] = yaml.load(contents, Loader=yaml.Loader)

        obj = cls()

        for key, value in data.items():
            setattr(obj, key, value)

        return obj

    @classmethod
    def dump_default(cls):
        return yaml.dump(
            dict(Config.dict(Config)),
            Dumper=yaml.Dumper,
        )


config_path = util.resolve("~/.config/venture.yaml")
if os.path.isfile(config_path):
    config = Config.from_file(config_path)
else:
    config = Config()
