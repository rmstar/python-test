import itertools
import os

def factors(n):
    return filter(lambda x: n % x == 0, itertools.takewhile(lambda y: y <= n, itertools.count(1)))

print(list(factors(48)))

def flatmap(f, items):
    return itertools.chain.from_iterable(map(f, items))

print(list(flatmap(os.listdir, ['/opt', '/Users'])))


