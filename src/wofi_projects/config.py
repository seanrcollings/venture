from typing import Dict
from .types import DirectorySchema


class Config:
    default = {
        "directories": [
            {
                "base": "/home/sean/sourcecode",
                "subs": [
                    "rust",
                ],
            },
            "/home/sean/sourcecode/crystal",
        ],
        "show_icons": True,
        "show_hidden": False,
        "show_files": True,
        "ui_provider": "wofi",
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
        self.ui_provider: str = (
            kwargs.get("ui_provider") or self.default["ui_provider"]
        )  # type
        self.wofi: Dict[str, str] = kwargs.get("wofi") or self.default["wofi"]  # type: ignore


config = Config()
