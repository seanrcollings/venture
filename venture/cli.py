from pathlib import Path
import subprocess
import arc
from rich import print
from xdg import xdg_config_home

from venture.browse import BrowseOption, BrowseList
from venture.config import Config, ProfileConfig
from venture import pango

arc.configure(environment="development")

cli = arc.namespace("venture")

DEFAULT_CONFIG_FILE = xdg_config_home() / "venture.toml"
# CONFIG_FILE = Path("config.toml")


@cli.subcommand()
def browse(
    profile_name: str = arc.Option(name="profile", short="p", default="default"),
    config_path: Path = arc.Option(
        name="config", short="c", default=DEFAULT_CONFIG_FILE
    ),
):
    config = Config.load(config_path)
    profile = config.browse.profiles.get(profile_name)
    if not profile:
        arc.err(f"No profile with name {profile_name!r} found in config")
        arc.exit(1)

    listing = BrowseList(config.browse)
    mapping = {
        format_option(l, config, profile): l["path"] for l in listing.discover(profile)
    }

    proc = subprocess.run(
        config.ui.exec,
        input="\n".join(mapping).encode("utf-8"),
        check=False,
        shell=True,
        capture_output=True,
    )

    choice = proc.stdout.decode("utf-8").strip()
    path = mapping.get(choice)

    if not path:
        arc.err(f"Provided input is invalid: {choice!r}")
        arc.exit(1)

    subprocess.Popen(
        profile.exec.format(path=path),
        shell=True,
        start_new_session=True,
    )


def format_option(
    option: BrowseOption,
    config: Config,
    profile: ProfileConfig,
) -> str:
    name = option["name"]
    icon = option["icon"]
    if config.ui.supports.pango and profile.show.icons:
        return f"{pango.span(icon.code, color=icon.color)} {name}"

    if profile.show.icons:
        return f"{icon.code} {name}"

    return name
