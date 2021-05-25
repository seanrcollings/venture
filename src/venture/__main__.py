import sys
import subprocess
import shlex
from arc import CLI

from .config import config
from .project_list import ProjectList
from .ui import get_ui_provider
from . import util

cli = CLI()


@cli.command()
def run():
    projects = ProjectList(config.directories).projects
    provider = get_ui_provider(config.ui_provider)
    choice = provider.run(projects.keys(), config)
    if choice == "":
        return

    project = projects[choice]
    command = config.exec.format(path=project.fullpath)
    command = shlex.split(command)
    subprocess.run(command, check=True)


@cli.command()
def dump():
    """Dump Default Config to
    ~/.config/venture.yaml
    """
    with open(util.resolve("~/.config/venture.yaml"), "w+") as f:
        f.write(config.dump_default())


def main():
    if len(sys.argv) <= 1:
        cli("run")
    else:
        cli()
