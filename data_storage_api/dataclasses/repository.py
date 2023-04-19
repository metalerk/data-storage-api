from typing import List
from dataclasses import dataclass
from .object import ObjectDataclass


@dataclass
class RepositoryDataclass:
    name: str
    data: List[ObjectDataclass]
