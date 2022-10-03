from dataclasses import dataclass


@dataclass
class My:
    f1: float
    f2: int
    f3: str

m = My(f2 = 1, f1 = 2.1, f3 = 'a')

print(m.f1, m.f2, m.f3)
a = 2
print(++a)
print(a)