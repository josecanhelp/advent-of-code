# %%
import math
import functools

input = [line.split() for line in open(
    'input-day6.txt', "r").read().split("\n\n")]


def getUnique(i):
    return set(i)


def getSimilars(i, j):
    return set(i) & set(j)


print(math.fsum((len(getUnique(x))
                 for x in (''.join(y) for y in input))))  # 6662

print(math.fsum((len(functools.reduce(getSimilars, x)) for x in input)))  # 3382
# %%
