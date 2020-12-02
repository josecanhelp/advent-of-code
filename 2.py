import math

input = open("input-day2.txt", "r")

def sledRentalPolicy(inputDict):
    return 1 if inputDict["low"] <= len(list(filter(lambda x: x == inputDict["needle"], list(inputDict["haystack"])))) <= inputDict["high"] else 0

def tobogganPolicy(inputDict):
    haystackList = list(inputDict["haystack"])
    lowIndex = inputDict["low"] - 1
    highIndex = inputDict["high"] - 1
    lowChar = '-' if (len(haystackList) - 1) < lowIndex else haystackList[lowIndex]
    highChar = '-' if (len(haystackList) - 1) < highIndex else haystackList[highIndex]
    return 1 if (lowChar == inputDict["needle"]) ^ (highChar == inputDict["needle"]) else 0


def generateDictFor(row):
    return {
        "low": int(row.split(" ")[0].split("-")[0]),
        "high": int(row.split(" ")[0].split("-")[1]),
        "needle": row.split(" ")[1].split(":")[0],
        "haystack": row.split(" ")[2].split("\n")[0],
    }

inputAsDict = list((generateDictFor(x) for x in input))
print(math.fsum((sledRentalPolicy(x) for x in inputAsDict))) # 603
print(math.fsum((tobogganPolicy(x) for x in inputAsDict))) # 404

