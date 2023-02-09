import os
from pathlib import Path
from pydantic import BaseModel
import toml
import arc

from .icons import default


class UISupportsConfig(BaseModel):
    pango: bool = False


class UiConfig(BaseModel):
    exec: str
    seperator: str = "\n"
    supports: UISupportsConfig


class CacheConfig(BaseModel):
    enabled: bool = True


class SharedShowConfig(BaseModel):
    icons: bool = True


class ProfileShowConfig(SharedShowConfig):
    hidden: bool = False
    files: bool = True
    directories: bool = True
    fullpath: bool = False


class ProfileConfig(BaseModel):
    paths: list[Path]
    exec: str
    exclude: list[str] = []
    show: ProfileShowConfig = ProfileShowConfig()


class BrowseConfig(BaseModel):
    profiles: dict[str, ProfileConfig]


class QuickLaunchEntryConfig(BaseModel):
    name: str
    path: str
    icon: str = default.code
    tags: list[str] = []


class QuickLaunchConfig(BaseModel):
    exec: str
    entries: list[QuickLaunchEntryConfig]
    show: SharedShowConfig = SharedShowConfig()


class Config(BaseModel):
    ui: UiConfig
    cache: CacheConfig
    browse: BrowseConfig
    quicklaunch: QuickLaunchConfig | None = None

    @classmethod
    def load(cls, filepath: os.PathLike):
        if not os.path.exists(filepath):
            raise arc.errors.ExecutionError(f"Config file not found: {filepath}")

        return cls(**toml.load(filepath))
