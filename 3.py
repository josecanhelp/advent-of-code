import math

input = open("input-day3.txt", "r")

def treeHit(row, rowNum):
    v = rowNum * 3
    i = v if v < 31 else (v % 31)
    return 1 if list(row)[i] == '#' else 0

print(math.fsum((treeHit(x.strip(), idx) for idx, x in enumerate(input))))
