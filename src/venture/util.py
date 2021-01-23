import os


def resolve(path: str) -> str:
    return os.path.expanduser(path)
