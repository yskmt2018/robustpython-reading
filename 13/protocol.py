from __future__ import annotations
from typing import Protocol


class Splittable(Protocol):
    cost: int
    name: str

    def split_in_half(self) -> tuple[Splittable, Splittable]:
        """ 実装不要 """
        ...


class BLTSandwich:
    def __init__(self):
        self.cost = 6.95
        self.name = "BLT"
        # このクラスは一人前のBLTサンドを作る
        ...
    
    def split_in_half(self) -> tuple[BLTSandwich, BLTSandwich]:
        # サンドイッチを半分に分割する方法
        # 斜めに切る、別々に包むなど
        # 2個のサンドイッチを返す
        ...
