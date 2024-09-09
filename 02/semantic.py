import datetime


def close_kitchen_if_past_cutoff_time1(point_in_time):
    if point_in_time >= closing_time():
        close_kitchen()
        log_time_closed(point_in_time)


def close_kitchen_if_past_cutoff_time2(point_in_time: datetime.datetime):
    if point_in_time >= closing_time():
        close_kitchen()
        log_time_closed(point_in_time)


# 以下、サンプル関数
def closing_time() -> datetime.datetime:
    return datetime.datetime(2024, 9, 10, 20, 30, 0, 0)


def close_kitchen():
    print('閉店です')


def log_time_closed(point_in_time: datetime.datetime):
    print(point_in_time)
