# %%
from parse import findall, search


def lineToTuple(line):
    return (search('{} bags', line)[0], [*findall('{:d} {} bag', line)])


luggageRules = dict(lineToTuple(x) for x in open('input-day7.txt'))


def checkBag(bag, needle):
    return any(color == needle or checkBag(color, needle) for count, color in luggageRules[bag])


def bagsToContainIn(bag):
    return sum(count * (bagsToContainIn(color) + 1) for count, color in luggageRules[bag])


print(sum(checkBag(x, 'shiny gold') for x in luggageRules))  # 265
print(bagsToContainIn('shiny gold'))  # 14177


# %%
