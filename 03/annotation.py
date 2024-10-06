import datetime
import random


def schedule_restaurant_open1(open_time, workers_needed):
    ...


def schedule_restaurant_open2(open_time: datetime.datetime, workers_needed: int):
    workers: list[str] = find_workers_available_for_time(open_time)
    # X人のシフトに入れる従業員からworkers_needed人を選ぶために
    # random.sampleを使う
    for worker in random.sample(workers, workers_needed):
        worker.schedule(open_time)


def find_workers_available_for_time(open_time: datetime.datetime) -> list[str]:
    workers = worker_database.get_all_workers()
    available_workers = [worker for worker in workers if is_available(worker)]
    if available_workers:
        return available_workers
    # 緊急時にはシフトに入れると登録した従業員のリストにフォールバックする
    emergency_workers = [
        worker for worker in get_emergency_workers() if is_available(worker)
    ]
    if emergency_workers:
        return emergency_workers
    # オーナーをシフトに入れる。他の人はオーナーに見つけてもらう
    return [OWNER]


OWNER = 'owner'
worker_database = None


def get_emergency_workers():
    ...


def is_available(worker):
    ...
