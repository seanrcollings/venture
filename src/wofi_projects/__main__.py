import subprocess
import shlex

from .config import config
from .project_list import ProjectList
from .ui import UIProvider, Wofi


def get_ui_provider(provider_str: str) -> UIProvider:
    if provider_str == "wofi":
        return Wofi()

    raise ValueError(f"{provider_str} is an unkown UI Provider")


def main():
    projects = ProjectList(config.directories).projects
    provider = get_ui_provider(config.ui_provider)
    choice = provider.run(projects.keys(), config)

    path = projects[choice]
    command = shlex.split(config.exec)
    command.append(path)
    subprocess.run(command, check=True)
