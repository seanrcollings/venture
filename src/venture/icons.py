from typing import Dict, Optional

# Load the icons

__icons: Dict[str, str] = {
    "directory": "",
    "default": "",
    "py": "\uf81f",
    "rb": "",
    "cr": "",
    "rs": "",
    "js": "",
}


def icon(name: str) -> Optional[str]:
    """Get an icon associated with a filename,
    returns the default if it doesn't exist"""
    name = name.lstrip(".")
    return __icons.get(name) or __icons.get("default")
