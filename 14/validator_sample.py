from typing import Optional

from pydantic.dataclasses import dataclass
from pydantic import constr, PositiveInt, conlist, validator


@dataclass
class AccountAndRoutingNumber:
    # 文字列の長さを指定した範囲に制限する
    account_number: constr(min_length=9, max_length=9)
    routing_number: constr(min_length=8, max_length=12)


@dataclass
class Address:
    address: constr(min_length=1)

# ... 省略 ...

@dataclass
class Dish:
    name: constr(min_length=1, max_length=16)
    price_in_cents: PositiveInt
    description: constr(min_length=1, max_length=80)
    picture: Optional[str] = None


@dataclass
class Restaurant:
    # 正規表現にマッチする文字列だけに制限する（この場合、英数字とスペースのみ）。
    name: constr(regex=r"^[a-zA-Z0-9 ]*$", min_length=1, max_length=16)
    owner: constr(min_length=1)
    address: constr(min_length=1)
    employees: list[Employee]
    dishes: list[Dish]
    number_of_seats: PositiveInt
    to_go: bool
    delivery: bool


@dataclass
class Restaurant2:
    name: constr(regex=r"^[a-zA-Z0-9 ]*$", min_length=1, max_length=16)
    owner: constr(min_length=1)
    address: constr(min_length=1)
    # このリストの要素はEmployee型の値に限られ、少なくとも2名の従業員が必要になる。
    employees: conlist(Employee, min_items=2)
    # このリストの要素はDish型の値に限られ、少なくとも3種類の料理が必要になる。
    dishes: conlist(Dish, min_items=3)
    number_of_seats: PositiveInt
    to_go: bool
    delivery: bool


@dataclass
class Restaurant3:
    name: constr(regex=r"^[a-zA-Z0-9 ]*$", min_length=1, max_length=16)
    owner: constr(min_length=1)
    address: constr(min_length=1)
    employees: conlist(Employee, min_items=2)
    dishes: conlist(Dish, min_items=3)
    number_of_seats: PositiveInt
    to_go: bool
    delivery: bool

    @validator("employees")
    def check_chef_and_server(cls, employees):
        if (any(e for e in employees if e.position == "Chef") and
            any(e for e in employees if e.position == "Server")):
                return employees
        raise ValueError("Must have at least one chef and one server")
