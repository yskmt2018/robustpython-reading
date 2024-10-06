def add_doubled_values(my_list: list[int]):
    """リストを受け付け、各要素の2倍の値を全体の末尾に追加する

    [1, 2, 3] -> [1, 2, 3, 2, 4, 6]
    """
    my_list.update([x * 2 for x in my_list])


add_doubled_values([1, 2, 3])
