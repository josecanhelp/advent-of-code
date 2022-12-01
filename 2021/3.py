import itertools
import math

input = list(open("input-day3.txt", "r"))

def treeHit(row, rowNum, multiplier = 3):
    return 1 if list(row)[(rowNum * multiplier) % 31] == '#' else 0

def slopeSlicer(rows, every = 1):
    return itertools.islice(rows, 0, None, every)

def treeHitsForPath(right = 1, down = 1):
    slopes = slopeSlicer(input, down)
    return math.fsum((treeHit(x, idx, right) for idx, x in enumerate(slopes)))

path1 = treeHitsForPath(3, 1) # 240
path2 = treeHitsForPath(1, 1)
path3 = treeHitsForPath(5, 1)
path4 = treeHitsForPath(7, 1)
path5 = treeHitsForPath(1, 2)
print(math.prod([path1, path2, path3, path4, path5])) # 2832009600
