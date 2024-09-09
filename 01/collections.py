class Cookbook: ...


def create_author_count_mapping1(cookbooks: list[Cookbook]):
    counter = {}
    for cookbook in cookbooks:
        if cookbook.author not in counter:
            counter[cookbook.author] = 0
        counter[cookbook.author] += 1
    return counter


# リスト
## リスト内包表記
ex_list = [x**2 for x in range(10000)]

# 文字列
ex_str = 'hello'

# ジェネレータ
## ジェネレータ式
ex_generator = (x**2 for x in range(10000))

# タプル
ex_tuple = ('RobustPython', 'pviafore', 359)

# 集合
## 集合内包表記
ex_set = {x**2 for x in range(10000)}

# 辞書
## 辞書内包表記
ex_dict = {x: x**2 for x in range(10000)}


from collections import defaultdict


def create_author_count_mapping(cookbooks: list[Cookbook]):
    counter = defaultdict(lambda: 0)
    for cookbook in cookbooks:
        counter[cookbook.author] += 1
    return counter


from collections import Counter


def create_author_count_mapping(cookbooks: list[Cookbook]):
    return Counter(book.author for book in cookbooks)
