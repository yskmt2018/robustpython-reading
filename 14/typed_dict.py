from typing import Literal, Optional, TypedDict, Union
import yaml


class AccountAndRoutingNumber(TypedDict):
    account_number: str
    routing_number: str


class BankDetails(TypedDict):
    bank_details: AccountAndRoutingNumber


AddressOrBankDetails = Union[str, BankDetails]

Position = Literal["Chef", "Sous Chef", "Host", "Server", "Delivery Driver"]


class Dish(TypedDict):
    name: str
    price_in_cents: int
    description: str
    picture: Optional[str]


class Employee(TypedDict):
    name: str
    position: Position
    payment_information: AddressOrBankDetails


class Restaurant(TypedDict):
    name: str
    owner: str
    address: str
    employees: list[Employee]
    dishes: list[Dish]
    number_of_seats: int
    to_go: bool
    delivery: bool


def load_restaurant(filename: str) -> Restaurant:
    with open(filename) as yaml_file:
        return yaml.safe_load(yaml_file)
