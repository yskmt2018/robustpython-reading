from __future__ import annotations


class Splittable:
    def __init__(self, cost, name):
        self.cost = cost
        self.name = name
    
    def split_in_half(self) -> tuple[Splittable, Splittable]:
        raise NotImplementedError("2分割のサポートが必要です")


class BLTSandwich(Splittable):
    pass


class Chili(Splittable):
    pass
