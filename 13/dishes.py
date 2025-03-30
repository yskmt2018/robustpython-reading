from __future__ import annotations
import math


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


class Chili:
    def __init__(self):
        self.cost = 4.95
        self.name = "チリコンカン"
        # このクラスは一人前のチリコンカンを作る
        ...
    
    def split_in_half(self) -> tuple[Chili, Chili]:
        # チリコンカンを半分に分割する方法
        # 別の容器によそい、トッピングを追加する
        # 2個のチリコンカンをよそった小鉢を返す
        ...


class BaconCheeseBurger:
    def __init__(self):
        self.cost = 11.95
        self.name = "ベーコンチーズバーガー"
        # このクラスはベーコンチーズバーガーを作る
        ...
    
    # 注意！ split_in_half メソッドなし


def split_dish(dish):
    """
    小盛のメソッド
    """
    dishes = dish.split_in_half()
    assert len(dishes) == 2
    for half_dish in dishes:
        half_dish.cost = math.ceil(half_dish.cost) / 2
        half_dish.name = "1/2 " + half_dish.name
    return dishes
