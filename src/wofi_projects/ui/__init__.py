from .wofi import Wofi
from .ui_provider import UIProvider


def get_ui_provider(provider_str: str) -> UIProvider:
    if provider_str == "wofi":
        return Wofi()

    raise ValueError(f"{provider_str} is an unkown UI Provider")
