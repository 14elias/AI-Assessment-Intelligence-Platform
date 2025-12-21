from dataclasses import dataclass
from typing import List


@dataclass
class Question:
    number: int
    text: str
    options: List[str]


@dataclass
class RejectedQuestion:
    raw_block: str
    reason: str
