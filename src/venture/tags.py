from pathlib import Path
from .icons import file_icon_map, filetype_icon
from .util import resolve, pango_span


def get_icon_tag(suffix):
    icon = filetype_icon(suffix)
    return pango_span(f"{icon.code}", color=icon.color) + f" { file_icon_map[suffix]}"


def get_tags(filepath: str, user_tags: list[str], no_default_tags=False):
    filepath = resolve(filepath)
    if no_default_tags:
        return set(user_tags)

    path = Path(filepath)
    tags = set(
        map(lambda tag: get_icon_tag(tag) if tag in file_icon_map else tag, user_tags)
    )

    extension = path.suffix.lstrip(".")

    if path.is_file() and extension in file_icon_map:
        tags.add(get_icon_tag(extension))
    if "config" in str(path.absolute()):
        tags.add(get_icon_tag("config"))

    return tags
