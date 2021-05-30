from typing import Any, Optional
import os
import yaml
from arc.utils import logger, timer

from .types import DirectorySchema, QuickLaunchEntry
from . import util

CONFIG_FILE = os.getenv("VENTURE_CONFIG") or util.resolve("~/.config/venture.yaml")

# This configuration design is super over-engineered,
# and I should have just gone with loading a dictionary and keeping it as a dict
# but eh, I'm not changing it now so it stays. (and it was kinda fun to build!)


class BrowseConfig(util.DictWrapper):
    exec: Optional[str]
    use_cache: bool
    show_files: bool
    show_hidden: bool
    show_icons: bool
    include_parent_folder: bool
    entries: DirectorySchema
    show_quicklaunch: bool


class QuickLaunchConfig(util.DictWrapper):
    exec: Optional[str]
    entries: dict[str, QuickLaunchEntry]


class Config:
    exec: str = "code -r {path}"
    ui: str = "rofi"

    browse: BrowseConfig = BrowseConfig(
        dict(
            exec="",
            show_quicklaunch=False,
            show_icons=True,
            show_hidden=False,
            show_files=True,
            use_cache=True,
            include_parent_folder=False,
        )
    )

    quicklaunch: QuickLaunchConfig = QuickLaunchConfig(dict(exec="", entries={}))

    def __iter__(self):
        yield from [
            (
                prop,
                dict(value)
                if isinstance(value := getattr(self, prop), util.DictWrapper)
                else value,
            )
            for prop in dir(self)
            if not prop.startswith("_") and not callable(getattr(self, prop))
        ]

    def get(self, item, default=None):
        return getattr(self, item, default)

    @classmethod
    @timer("Loading Config")
    def from_file(cls, file):
        with open(file) as f:
            contents = f.read()
            data: dict[str, Any] = yaml.load(contents, Loader=yaml.CLoader)

        obj = cls()
        if not data:
            return obj

        for key, value in data.items():
            if key == "ui_provider" and value not in dir(obj):
                setattr(obj, value, {})

            if isinstance(value, dict):
                setattr(obj, key, util.DictWrapper(obj.get(key) | value))
            else:
                setattr(obj, key, value)

        return obj

    def write(self, default: bool = False):
        """Write Configuration to file in yaml format"""
        if default:
            data = dict(Config())
        else:
            data = dict(self)

        with open(CONFIG_FILE, "w") as f:
            f.write(yaml.dump(data, Dumper=yaml.CDumper))

    @staticmethod
    def exists() -> bool:
        return os.path.exists(CONFIG_FILE)


if os.path.isfile(CONFIG_FILE):
    logger.debug("Loading %s", CONFIG_FILE)
    config: Config = Config.from_file(CONFIG_FILE)
else:
    logger.debug("Config File not found, loading defaults")
    config = Config()
