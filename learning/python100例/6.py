from functools import lru_cache

#@lru_cache(None)
def f(n):
    assert n >= 0
    return n if n <= 1 else f(n - 1) + f(n - 2)

i = int(input('输入斐波那契数列个数：'))
for x in range(0,i):
    print(f(x))