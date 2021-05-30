# pylint: disable=inherit-non-class
from typing import List, Union, Dict, TypedDict, Optional


DirectorySchema = List[Union[str, Dict[str, Union[str, List[str]]]]]


class QuickLaunchEntry(TypedDict):
    path: str
    icon: str
    tags: Optional[list[str]]
