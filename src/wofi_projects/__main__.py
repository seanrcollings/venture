from typing import Dict, List, cast

import subprocess
import shlex

from .config import config
from .project_list import ProjectList


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
    projects = ProjectList(config.directories).projects
    choice = create_menu(projects.keys())
    if choice == "":
        return

    path = projects[choice]
    command = shlex.split(config.exec)
    command.append(path)
    subprocess.run(command, check=True)
