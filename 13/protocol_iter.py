from collections.abc import Iterator, MutableSequence
from random import shuffle


class ShuffleIterator:
    def __init__(self, sequence: MutableSequence):
        self.sequence = list(sequence)
        shuffle(self.sequence)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.sequence:
            raise StopIteration
        return self.sequence.pop(0)


my_list = [1, 2, 3, 4]
iterator: Iterator = ShuffleIterator(my_list)

for num in iterator:
    print(num)
