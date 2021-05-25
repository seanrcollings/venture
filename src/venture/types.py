from typing import List, Union, Dict, TypedDict


DirectorySchema = List[Union[str, Dict[str, Union[str, List[str]]]]]

# pylint: disable=inherit-non-class
class QuickLaunchEntry(TypedDict):
    path: str
    icon: str


QuickLaunchSchema = Dict[str, QuickLaunchEntry]
