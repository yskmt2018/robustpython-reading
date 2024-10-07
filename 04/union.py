from typing import Union, Optional
from dataclasses import dataclass


class HotDog: ...

class Pretzel: ...


def dispense_snack() -> HotDog:
    if not are_ingredients_available():
        raise RuntimeError('材料が足りません')
    if order_interrupted():
        raise RuntimeError('注文が取り消されました')
    return create_hot_dog()


def dispense_snack(user_input: str) -> Union[HotDog | Pretzel]:
    if user_input == 'ホットドッグ':
        return dispense_hot_dog()
    elif user_input == 'プレッツェル':
        return dispense_pretzel()
    raise RuntimeError('入力が無効 ここに到達してはならない')


def place_holder() -> Optional[HotDog]:
    order = get_order()
    result = dispense_snack(order.name)
    if result is None:
        print('エラーが発生しました' + result)
        return None
    # HotDogを返す
    return result


@dataclass
class Snack:
    name: str
    condiments: set[str]
    error_code: int
    disposed_of: bool


Snack('ホットドッグ', {'マスタード', 'ケチャップ'}, 5, False)


def serve(snack):
    # 何か問題が起きたら早い段階で制御を返す
    if snack.disposed_of:
        return
    ...


@dataclass
class Error:
    error_code: int
    disposed_of: bool


@dataclass
class Snack2:
    name: str
    condiments: set[str]


snack: Union[Snack2 | Error] = Snack2('ホットドッグ', {'マスタード', 'ケチャップ'})

snack = Error(5, True)

def are_ingredients_available(): ...

def order_interrupted(): ...

def create_hot_dog(): ...

def dispense_hot_dog(): ...

def dispense_pretzel(): ...

def get_order(): ...
