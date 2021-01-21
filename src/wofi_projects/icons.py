from typing import Dict, Optional

# Load the icons

__icons: Dict[str, str] = {
    "directory": "",
    "default": "",
    "py": "",
    "rb": "",
    "cr": "",
    "rs": "",
    "js": "",
}


def icon(name: str) -> Optional[str]:
    """Get an icon associated with a filename,
    returns None if it doesn't exist"""
    name = name.lstrip(".")
    return __icons.get(name)
