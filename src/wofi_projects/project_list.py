from typing import Dict, List, Union, cast, Optional
from pathlib import Path
import subprocess
import shlex
import os

DirectorySchema = List[Union[str, Dict[str, Union[str, List[str]]]]]


class Config:
    default = {
        "directories": [
            "/home/sean/sourcecode/rust",
            "/home/sean/sourcecode/crystal",
        ],
        "show_icons": True,
        "show_hidden": False,
        "show_files": True,
        "wofi": {
            "config": "/home/sean/.config/wofi/projects/config",
            "stylesheet": "/home/sean/.config/wofi/projects/style.css",
        },
        "exec": "code -r",
    }

    def __init__(self, **kwargs):

        self.directories: DirectorySchema = (
            kwargs.get("directories") or self.default["directories"]  # type: ignore
        )
        self.exec: str = kwargs.get("show_icons") or self.default["exec"]  # type: ignore
        self.show_icons: bool = kwargs.get("show_icons") or self.default["show_icons"]  # type: ignore
        self.show_hidden: bool = (
            kwargs.get("show_hidden") or self.default["show_hidden"]  # type: ignore
        )
        self.show_files: bool = kwargs.get("show_files") or self.default["show_files"]  # type: ignore
        self.wofi: Dict[str, str] = kwargs.get("wofi") or self.default["wofi"]  # type: ignore


config = Config()

EXCLUDED_DIRS = [
    "node_modules",
    ".git",
]


ICONS = {
    "directory": "",
    "default": "",
    "py": "",
    "rb": "",
    "cr": "",
    "rs": "",
    "js": "",
}


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
            elif isinstance(
                directory, dict
            ):  # handle a base directory and it's sub-dirs
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

    def get_icon(self, filetype: str):
        """Returns the icon associated with a specific file type"""
        if not config.show_icons:
            return None

        return ICONS.get(filetype.lstrip(".")) or ICONS.get("default")


def get_commandline_args():
    args = []
    wofi_conf = cast(Dict[str, str], config.wofi)
    if conf := wofi_conf.get("config"):
        args.append("--conf")
        args.append(conf)
    if style := wofi_conf.get("stylesheet"):
        args.append("--style")
        args.append(style)

    return args


def create_menu(projects: List[str]) -> str:
    """Creates the menu based on provided projects list, returns the user's choice

    :param projects: list of strings to populate the mnu with
    """
    proc = subprocess.Popen(
        ["wofi", "--dmenu", *get_commandline_args()],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    output = proc.communicate(bytes("\n".join(projects), "utf-8"))[0]
    choice = output.decode("utf-8").strip("\n")
    return choice


def main():
    directories = cast(DirectorySchema, config.directories)
    projects = ProjectList(directories).projects
    choice = create_menu(projects.keys())
    if choice == "":
        return

    path = projects[choice]
    command = shlex.split(config.exec)
    command.append(path)
    subprocess.run(command, check=True)


main()