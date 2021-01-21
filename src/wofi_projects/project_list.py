from typing import Dict, List, cast, Optional
from pathlib import Path
import os

from .types import DirectorySchema
from .config import config
from .icons import icon

EXCLUDED_DIRS = [
    "node_modules",
    ".git",
]


class ProjectList:
    def __init__(self, directories: DirectorySchema):
        self.dirs = directories
        self.projects = self.handle_directories()

    def handle_directories(self):
        # contains mappings between display name: full path
        projects: Dict[str, str] = {}

        for directory in self.dirs:
            if directory in EXCLUDED_DIRS:
                continue

            if isinstance(directory, str):  # handle a single directory
                projects |= {  # type: ignore
                    f"{icon + '  ' if icon else ''}{name.removeprefix(directory + '/')}": name
                    for icon, name in self.get_projects(directory)
                }
            elif isinstance(directory, dict):
                # handle a base directory and it's sub-dirs
                base = cast(str, directory["base"])
                subs = cast(List[str], directory["subs"])
                directories = [f"{base}/{sub.lstrip('/')}" for sub in subs]
                directories.append(base)
                for directory in directories:
                    projects |= {  # type: ignore
                        f"{icon + '  ' if icon else ''}{name.removeprefix(base + '/')}": directory
                        for icon, name in self.get_projects(directory, base)
                    }

        return projects

    def get_projects(self, directory: str, prefix: Optional[str] = None):
        """Gets all the projects / files from the specified directory
        appends icons to each path if `config['show_icons']` is `True`
        """

        prefix = prefix or directory

        for obj in os.scandir(directory):
            path = Path(obj.path)
            if (path.name.startswith(".") and not config.show_hidden) or (
                path.is_file() and not config.show_files
            ):
                continue

            if path.is_dir():
                yield self.get_icon("directory"), str(path)
            elif path.is_file():
                yield self.get_icon(path.suffix.lstrip(".")), str(path)

    def get_icon(self, filetype: str) -> Optional[str]:
        """Returns the icon associated with a specific file type,
        returns none if config.show_icons is set to False"""
        if not config.show_icons:
            return None

        return icon(filetype) or icon("default")
