# %%
import re
import math

input = [line.split(" contain ") for line in open(
    'test.txt', "r").read().split("\n") if line != ""]


# def makeTuple(luggageRule):
#     return re.compile(r'\d? ?(\w+) (\w+) bags?.?').match(luggageRule).groups()

def makeTuple(luggageRule, withCount=False):
    m = re.match(
        r'(?P<count>\d)? ?(?P<descriptor>\w+) (?P<color>\w+) bags?.?', luggageRule)
    return (m.group('count'), m.group('descriptor'), m.group('color')) if withCount else (m.group('descriptor'), m.group('color'))


luggageRules = {}
luggageRulesWithCount = {}

for item in input:
    luggageRules.update({
        makeTuple(item[0]): [makeTuple(x) for x in item[1].split(', ') if makeTuple(x) != ('no', 'other')]
    })

for item in input:
    luggageRulesWithCount.update({
        makeTuple(item[0]): [makeTuple(x, True) for x in item[1].split(', ') if makeTuple(x) != ('no', 'other')]
    })

outerBags = []
innerBags = []


def countOuterBags(tup):
    for key, val in luggageRules.items():
        if tup in val:
            outerBags.append(key)
            countOuterBags(key)


def countInnerBags(tup):
    for item in luggageRulesWithCount[(tup[1], tup[2])]:
        innerBags.append(int(int(item[0]) * tup[0]))
        countInnerBags(item)


if __name__ == "__main__":
    countOuterBags(('shiny', 'gold'))
    countInnerBags((1, 'shiny', 'gold'))
    # print(len(set(outerBags)))
    print(math.fsum(innerBags))
# %%
