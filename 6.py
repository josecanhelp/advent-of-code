# %%
import math
import functools

with open("input-day6.txt", "r") as f:
    input = [line.split() for line in f.read().strip().split("\n\n")]


def getUnique(i):
    return set(i)


def findSimilarities(i, j):
    return set(i) & set(j)


print(math.fsum((len(getUnique(x))
                 for x in (''.join(x) for x in input))))  # 3382
print(math.fsum([len(functools.reduce(findSimilarities, x)) for x in input]))
# %%
