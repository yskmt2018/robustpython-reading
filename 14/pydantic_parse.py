from pydantic import StrictInt
from pydantic.dataclasses import dataclass


@dataclass
class Model:
    value: int


Model(value="123")  # valueは整数の123になる
Model(value=5.5)  # valueは5に切り捨てられる


@dataclass
class Model2:
    value: StrictInt


x = Model2(value="0023").value  # エラーが返される
