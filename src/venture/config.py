import os
import yaml
from arc.utils import logger, timer
from pydantic import BaseModel

from .types import DirectorySchema, QuickLaunchEntry
from . import util
from .types import OpenContext


CONFIG_FILE = os.getenv("VENTURE_CONFIG") or util.resolve("~/.config/venture.yaml")


class BrowseConfig(BaseModel):
    exec: str = ""
    use_cache: bool = True
    show_files: bool = True
    show_hidden: bool = False
    show_icons: bool = True
    include_parent_folder: bool = True
    entries: DirectorySchema = ["~"]
    show_quicklaunch: bool = False


class QuickLaunchConfig(BaseModel):
    exec: str = ""
    entries: dict[str, QuickLaunchEntry] = {}


class Config(BaseModel):
    exec: str = "code -r {path}"
    args: dict[str, str] = {}
    ui: str = "rofi"
    browse: BrowseConfig = BrowseConfig()
    quicklaunch: QuickLaunchConfig = QuickLaunchConfig()

    def get_exec(self, open_context: OpenContext = None):
        if open_context is OpenContext.BROWSE:
            exec_str = self.browse.exec
        elif open_context is OpenContext.QUICK_LAUNCH:
            exec_str = self.quicklaunch.exec
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

        return cls(**yaml.load(contents, Loader=yaml.CLoader))

    def write(self, default: bool = False):
        """Write Configuration to file in yaml format"""
        if default:
            data = Config().dict()
        else:
            data = self.dict()

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
