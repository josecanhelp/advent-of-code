# %%
import math
import functools

input = list(open("input-day6.txt", "r"))


def removeNewline(el):
    return el.replace('\n', '')


def group(seq, sep):
    g = []
    for el in seq:
        if el == sep:
            yield g
            g = []
        if el != sep:
            g.append(removeNewline(el))
    yield g


def group2(seq, sep):
    g = []
    for el in seq:
        if el == sep:
            yield g
            g = []
        if el != sep:
            g.append(list(removeNewline(el)))
    yield g


result = list(group(input, '\n'))
result2 = list(group2(input, '\n'))

a = (''.join(x) for x in result)
print(math.fsum((len(list(set(list(x)))) for x in a)))  # 3382


e = []
for item in result2:
    e.append(len(functools.reduce(lambda i, j: set(i) & set(j), item)))

print(math.fsum(e))  # 3382

# %%
