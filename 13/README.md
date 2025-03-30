# 13 章 プロトコル

## 13.1 2 つの型システムの間の緊張関係

- [サンプルコード](./dishes.py)

* データ型の構造を基礎とする「構造的部分型」、データ型の名前を基礎とする「名目的部分型」

```python
def split_dish(dish: ???) -> ???:
    pass
```

### 13.1.1 データ型を指定しないか Any を使う

```python
def split_dish(dish: Any):
    pass
```

### 13.1.2 Union を使う

```python
def split_dish(dish: Union[BLTSandwich, Chili]):
    pass
```

### 13.1.3 継承を使う

- [サンプルコード](./dishes_extends.py)

```python
def split_dish(dish: Splittable):
    pass

def split_dish(dish: Splittable) -> tuple[Splittable, Splittable]:
    pass
```

#### 13.1.3.1 ミックスインを使う

```python
class BLTSandwich(Shareable, PickUppable, Substitutable, Splittable):
    pass
```

## 13.2 プロトコル

- [サンプルコード](./protocol_iter.py)

### 13.2.1 プロトコルの定義

- [サンプルコード](./protocol.py)

```python
def split_dish(dish: Splittable) -> tuple[Splittable, Splittable]:
    pass
```

## 13.3 高度な用法

### 13.3.1 複合プロトコル

```python
StandardLunchEntry = Union[Splittable, Shareable, Substitutable, PickUppable]

class StandardLunchEntry(Splittable, Shareable, Substitutable, PickUppable, Protocol):
    pass

# プロトコルを明示的に継承する必要はないが、
# ここでは意図を明確にするために継承している
class BLTSandwich(StandardLunchEntry):
    pass
```

### 13.3.2 実行時チェックできるプロトコル

- [サンプルコード](./protocol_runtime.py)

### 13.3.3 プロトコルを満たすモジュール

- [Restaurant](./restaurant.py)
- [Load Restaurant](./load_restaurant.py)
- [Loading Module](./loading_module.py)
