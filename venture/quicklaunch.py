from venture.config import Config, QuickLaunchConfig, QuickLaunchEntryConfig
from venture.icons import iconize
from venture import pango


def format_option(
    config: Config,
    ql_config: QuickLaunchConfig,
    entry: QuickLaunchEntryConfig,
):
    ui = ql_config.ui
    format_string = entry.format or ql_config.format
    format_args = entry.dict()

    format_args["icon"] = iconize(format_args["icon"], colored=ui.supports.pango)
    tags = ", ".join(
        iconize(tag, ui.supports.pango) for tag in format_args["tags"] if tag
    )
    format_args["tags"] = tags

    return format_string.format(**format_args)