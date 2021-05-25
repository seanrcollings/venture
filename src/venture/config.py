from typing import Any
import types
import os
import yaml

from .types import DirectorySchema
from . import util


class Config:
    directories: DirectorySchema = ["~"]
    exec: str = "code -r"
    ui_provider: str = "rofi"
    show_icons: bool = True
    show_hidden: bool = False
    show_files: bool = True
    include_parent_folder: bool = False
    wofi: dict[str, str] = {}
    rofi: dict[str, str] = {}
    dmenu: dict[str, str] = {}

    def __getitem__(self, item):
        return getattr(self, item)

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
            {
                key: getattr(cls, key)
                for key in [
                    prop
                    for prop in dir(cls)
                    if not prop.startswith("_")
                    and not isinstance(getattr(cls, prop), types.MethodType)
                ]
            },
            Dumper=yaml.Dumper,
        )


config_path = util.resolve("~/.config/venture.yaml")
if os.path.isfile(config_path):
    config = Config.from_file(config_path)
else:
    config = Config()
