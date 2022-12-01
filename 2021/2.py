import math
import re

input = open("input-day2.txt", "r")

def sledRentalPolicy(row):
    return 1 if int(row["low"]) <= len(list(filter(lambda x: x == row["needle"], list(row["haystack"])))) <= int(row["high"]) else 0

def tobogganPolicy(row):
    haystackList = list(row["haystack"])
    lowIndex = row["lowindex"]
    highIndex = row["highindex"]
    lowChar = '-' if (len(haystackList) - 1) < lowIndex else haystackList[lowIndex]
    highChar = '-' if (len(haystackList) - 1) < highIndex else haystackList[highIndex]
    return 1 if (lowChar == row["needle"]) ^ (highChar == row["needle"]) else 0

def indexedChars(row):
    return row
    #  return (list(row['haystack'])[row['lowIndex']], list(row['haystack'])[row['lowIndex']])

def dictForRow(row):
    matches = re.match(r"(?P<low>\d+)\-(?P<high>\d+) (?P<needle>\w{1})\: (?P<haystack>\w+)", row)
    return {
        "low": int(matches['low']),
        "lowindex": int(matches['low']) - 1,
        "high": int(matches['high']),
        "highindex": int(matches['high']) - 1,
        "needle": matches['needle'],
        "haystack": matches['haystack'],
    }

inputAsDict = list((dictForRow(x) for x in input))

for item in indexedChars(inputAsDict):
    print(item)
#  print(list(inputAsDict))
#  print(math.fsum((sledRentalPolicy(x) for x in inputAsDict))) # 603
#  print(math.fsum((tobogganPolicy(x) for x in inputAsDict))) # 404

