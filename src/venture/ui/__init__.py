from .dmenu_like import dmenu_like_menus
from .ui_provider import UIProvider


def get_ui_provider(provider_str: str) -> UIProvider:
    if provider_str in dmenu_like_menus:
        return dmenu_like_menus[provider_str]()

    raise ValueError(f"{provider_str} is an unkown UI Provider")
