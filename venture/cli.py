import typing as t
from pathlib import Path
import arc
from rich import print
from xdg import xdg_config_home

from venture import browse, ext, quicklaunch
from venture.config import Config, UiConfig

DEFAULT_CONFIG_FILE = xdg_config_home() / "venture.toml"

arc.configure(environment="development")
cli = arc.namespace("venture")


@arc.group
class SharedArgs:
    config_path: Path = arc.Option(
        name="config",
        short="c",
        default=DEFAULT_CONFIG_FILE,
        desc="Path to the config file to load",
    )


@cli.subcommand(("browse", "b"))
def browse_command(
    args: SharedArgs,
    profile_name: str = arc.Option(name="profile", short="p", default="default"),
) -> None:
    """Launch a particular browse profile"""
    config = Config.load(args.config_path)
    profile = config.browse.profiles.get(profile_name)
    if not profile:
        arc.err(f"No profile with name {profile_name!r} found in config")
        arc.exit(1)

    ui = t.cast(UiConfig, profile.ui or config.browse.ui)

    listing = browse.BrowseList(config.browse)
    mapping = {
        browse.format_option(ui.response_format or ui.format, l, ui): l["path"]
        for l in listing.discover(profile)
    }

    lst = (
        mapping.keys()
        if ui.response_format is None
        else (browse.format_option(ui.format, l, ui) for l in listing.discover(profile))
    )

    choice = ext.run_ui(ui, lst)
    path = mapping.get(choice)

    if not path:
        arc.err(f"Provided input is invalid: {choice!r}")
        arc.exit(1)

    ext.run_exec(profile.exec, path)


@cli.subcommand(("quicklaunch", "q"))
def quicklaunch_command(args: SharedArgs) -> None:
    config = Config.load(args.config_path)
    ql_config = config.quicklaunch
    mapping = {
        quicklaunch.format_option(config, ql_config, entry): entry
        for entry in ql_config.entries
    }

    choice = ext.run_ui(ql_config.ui, mapping)

    entry = mapping.get(choice)

    if not entry:
        arc.err(f"Provided input is invalid: {choice!r}")
        arc.exit(1)

    ext.run_exec(entry.exec or ql_config.exec, entry.path)
