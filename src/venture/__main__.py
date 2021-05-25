import subprocess
import shlex
from arc import CLI, ExecutionError

from .config import config
from .project_list import ProjectList
from .ui import get_ui_provider
from . import util

cli = CLI()


def pick(items, pick_config) -> str:
    provider = get_ui_provider(pick_config.ui_provider)
    choice = provider.run(items, config)
    if choice == "":
        raise ExecutionError("No Option Picked")

    return choice


def execute(path: str):
    command = config.exec.format(path=path)
    command = shlex.split(command)
    subprocess.run(command, check=True)


@cli.base()
@cli.command()
def run():
    """Open the venture selection menu"""
    breakpoint()
    projects = ProjectList(config.directories).projects
    choice = pick(projects.keys(), config)
    project = projects[choice]
    execute(project.fullpath)


@cli.command()
def quicklaunch():
    """Open the Quick Launch Menu"""

    items = {
        f"{item.get('icon', ''):<2} {item['name']}": item for item in config.quicklaunch
    }
    choice = pick(items.keys(), config)
    item = items[choice]
    execute(item["path"])


@cli.command()
def dump():
    """Dump Default Config to
    ~/.config/venture.yaml
    """
    with open(util.resolve("~/.config/venture.yaml"), "w+") as f:
        f.write(config.dump_default())
