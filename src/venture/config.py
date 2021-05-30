from typing import Any, Optional
import os
import yaml
from arc.utils import logger, timer

from .types import DirectorySchema, QuickLaunchEntry
from . import util
from .types import OpenContext

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
                dict(value) if issubclass(value.__class__, util.DictWrapper) else value,
            )
            for prop in dir(self)
            if not prop.startswith("_")
            and (value := getattr(self, prop))
            and not callable(value)
        ]

    def get(self, item, default=None):
        return getattr(self, item, default)

    def get_exec(self, open_context: OpenContext = None):
        if open_context is OpenContext.BROWSE:
            exec_str = self.browse.get("exec", self.exec)
        elif open_context is OpenContext.QUICK_LAUNCH:
            exec_str = self.quicklaunch.get("exec", self.exec)
        else:
            return self.exec

        if not exec_str:
            return self.exec

        return exec_str

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
