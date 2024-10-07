from dataclasses import dataclass
from typing import Literal


@dataclass
class Error:
    error_code: Literal[1, 2, 3, 4, 5]
    disposed_of: bool


@dataclass
class Snack:
    name: Literal['プレッツェル', 'ホットドッグ', 'ベジーバーガー']
    condiments: set[Literal['マスタード', 'ケチャップ']]


Error(0, False)
Snack('無効', set())
Snack('プレッツェル', {'マスタード', 'レリッシュ'})
