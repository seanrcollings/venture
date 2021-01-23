import subprocess
import shlex

from .config import config
from .project_list import ProjectList
from .ui import get_ui_provider


def main():
    projects = ProjectList(config.directories).projects
    provider = get_ui_provider(config.ui_provider)
    choice = provider.run(projects.keys(), config)
    if choice == "":
        return

    path = projects[choice]
    print(repr(path))
    # command = shlex.split(config.exec)
    # command.append(path)
    # subprocess.run(command, check=True)
