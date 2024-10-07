from typing import NewType


class HotDog:
    """提供できない状態のホットドッグを表すために使う"""
    pass


# 注意: ReadyToServeHotDogはprepare_for_serving以外の方法で作らないこと
ReadyToServeHotDog = NewType('ReadyToServeHotDog', HotDog)


def dispense_to_customer(hot_dog: ReadyToServeHotDog):
    # 提供できる状態のホットドッグだけを受け付けなければならない
    ...


def prepare_for_serving(hot_dog: HotDog) -> ReadyToServeHotDog:
    assert not hot_dog.is_plated(), 'ホットドッグが皿に乗っていてはいけません'
    hot_dog.put_on_plate()
    hot_dog.add_napkins()
    return ReadyToServeHotDog(hot_dog)


def make_snack():
    dispense_to_customer(ReadyToServeHotDog(HotDog()))
