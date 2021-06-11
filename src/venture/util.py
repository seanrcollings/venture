import os
import functools

import ujson


def resolve(path: str) -> str:
    return os.path.abspath(os.path.expanduser(path))


def pango_span(content, **kwargs):
    return (
        "<span "
        + " ".join(f'{key}="{value}"' for key, value in kwargs.items())
        + f">{content}</span>"
    )


def catch(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            raise Cache.CacheError(f"Cache {func.__name__} failed") from e

    return wrapper


class Cache:
    cache_path = "/tmp/venture-cache"
    meta: dict[str, str] = {}
    data: dict[str, str] = {}

    class CacheError(Exception):
        ...

    @classmethod
    @catch
    def read(cls):
        with open(cls.cache_path, "r") as f:
            data = ujson.loads(f.read())
            cls.meta = data["meta"]
            cls.data = data["data"]
            return cls.data

    @classmethod
    @catch
    def write(cls, data: dict):
        with open(cls.cache_path, "w") as f:
            f.write(ujson.dumps(data, ensure_ascii=False))

    @classmethod
    def exists(cls):
        return os.path.isfile(cls.cache_path)


def confirm(message: str):
    result = {
        "y": True,
        "n": False,
    }
    print(f"{message} [Y/N]")
    while True:
        user_input = input("> ").lower()
        if user_input in result:
            return result[user_input]
        print("Not understood, please type 'y' or 'n'")
