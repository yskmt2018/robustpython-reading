from typing import Protocol

from lunch import LunchEntry, Menu, StandardLunchEntry


class Restaurant(Protocol):
    name: str
    address: str
    standard_lunch_entries: list[StandardLunchEntry]
    other_entries: list[LunchEntry]

    def render_menu(self) -> Menu:
        """ 実装不要 """
        pass


def load_restaurant(restaurant: Restaurant):
    # レストランを読み込むコード
    pass
