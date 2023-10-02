from enum import StrEnum, auto

from pydantic import BaseModel


class CalcAction(BaseModel):
    a: int
    b: int


class ActionExtra(StrEnum):
    ONE = auto()
    TWO = auto()
