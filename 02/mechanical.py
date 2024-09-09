from binascii import hexlify
from ctypes import string_at
from sys import getsizeof


a = 0b01010000_01000001_01010100
print(a)
# 5259604

# メモリに格納されている変数の中身を表示する
print(hexlify(string_at(id(a), getsizeof(a))))
# b'03000000000000001028da48ff7f0000080000000000000054415000'

text = 'PAT'
print(hexlify(string_at(id(text), getsizeof(text))))
# b'ffffffff00000000705fda48ff7f00000300000000000000f793c864d0be94aa660000000000000050415400'

# これらの16進数文字列は、オブジェクトが格納されているメモリ位置（アドレス）を示す
## 組み込み関数 id() はオブジェクトの識別子を意味する整数を返す関数
