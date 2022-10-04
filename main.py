from dataclasses import dataclass
from sortedcontainers import SortedList


arr = [1, 2, 3, 4]
it = iter(arr)

for i in range(5):
    val = next(it)
    print(val)

sl = SortedList([(1, 0), (2, 3)])

print(sl.pop(0))
print(sl.pop(0))
print(sl.pop(0))

d = {'a': 1, 'c': 3}


for v in d.values():
    print(v)