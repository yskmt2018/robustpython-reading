from __future__ import annotations
from typing import runtime_checkable, Protocol


@runtime_checkable
class Splittable(Protocol):
    cost: int
    name: str

    def split_in_half(self) -> tuple[Splittable, Splittable]:
        pass


class BLTSandwich:
    pass


assert isinstance(BLTSandwich(), Splittable)
