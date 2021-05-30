# pylint: disable=inherit-non-class
from typing import List, Union, Dict


DirectorySchema = List[Union[str, Dict[str, Union[str, List[str]]]]]
