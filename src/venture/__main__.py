from __future__ import annotations
import subprocess
import shlex
from typing import Mapping
from arc import CLI, ExecutionError, CommandType as ct
from arc.color import fg, effects

from .config import config
from .project_list import ProjectList
from .ui import get_ui_provider, OpenContext
from .ui.ui_provider import T
from . import util

cli = CLI()


def pick(items: Mapping[str, T], pick_config, open_context: OpenContext) -> T:
    provider_type = get_ui_provider(pick_config.ui_provider, open_context)
    provider = provider_type(items, config)
    choice: T | None = provider.run()
    if not choice:
        raise ExecutionError("No Valid Option Picked")

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
    choice = pick(projects, config, OpenContext.DEFAULT)
    execute(choice.fullpath)


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
    choice = pick(config.quicklaunch, config, OpenContext.QUICK_LAUNCH)
    execute(choice["path"])


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
    config.quicklaunch[name] = {"path": path, "icon": icon, "tags": []}
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
