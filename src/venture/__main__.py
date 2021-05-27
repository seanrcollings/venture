import subprocess
import shlex
from arc import CLI, ExecutionError, CommandType as ct
from arc.color import fg, effects

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
    command = config.exec.format(path=util.resolve(path))
    command = shlex.split(command)
    subprocess.run(command, check=True)


@cli.base()
@cli.command()
def run():
    """Open the venture selection menu"""
    projects = ProjectList(config.directories).projects
    choice = pick(projects.keys(), config)

    if choice not in projects:
        raise ExecutionError(f"{choice} is not a valid choice")

    project = projects[choice]
    execute(project.fullpath)


@cli.command()
def dump():
    """Dump Default Config to
    ~/.config/venture.yaml
    """
    with open(util.resolve("~/.config/venture.yaml"), "w+") as f:
        f.write(config.dump_default())


@cli.command()
def quicklaunch():
    """Open the Quick Launch Menu"""

    items = {
        f"{item.get('icon', ''):<2} {name}": item
        for name, item in config.quicklaunch.items()
    }
    choice = pick(items.keys(), config)

    if choice not in items:
        raise ExecutionError(f"{choice} is not a valid choice")

    item = items[choice]

    execute(item["path"])


@quicklaunch.subcommand("list")
def list_quicklaunch():
    """List quicklaunch items"""
    if len(config.quicklaunch) == 0:
        print(
            "No quick-launch items, add one with "
            f"{fg.GREEN}quicklaunch:add{effects.CLEAR}"
        )
        return

    print("Quicklaunch Items:")
    for name, values in config.quicklaunch.items():
        print(
            f"- {values['icon']}  {name} {fg.BLACK.bright}({values['path']}){effects.CLEAR}"
        )


@quicklaunch.subcommand()
def add(name: str, path: str, icon: str = None):
    """\
    Add a new item to the Quick Launch Menu

    Arguments:
    name=NAME  Display name for the quick-launch entry
    path=PATH  File path to launch when the entry is picked
    icon=ICON  Icon to display along with the name, optional
    """
    config.quicklaunch[name] = {"path": path, "icon": icon}
    with open(util.resolve("~/.config/venture.yaml"), "w+") as f:
        f.write(config.dump())

    print(f"{fg.GREEN}{name} Added!{effects.CLEAR}")


@quicklaunch.subcommand(command_type=ct.POSITIONAL)
def remove(name: str):
    """"Remove an item from the Quick Launch Menu"""
    config.quicklaunch.pop(name)
    with open(util.resolve("~/.config/venture.yaml"), "w+") as f:
        f.write(config.dump())
    print(f"{fg.GREEN}{name} Removed!{effects.CLEAR}")
