# %%
input = list(open("input-day5.txt", "r"))

# Convert ticket string into dict of binary strings


def splitTicket(line):
    return {
        'row': line[0:7].replace("F", "0").replace("B", "1"),
        'col': line[-4::].rstrip("\n").replace("L", "0").replace("R", "0")
    }

# Convert binary strings to int and generate Seat ID


def getSeatId(line):
    return int(splitTicket(line)['row'], 2) * 8 + int(splitTicket(line)['col'], 2)


maxSeatId = max(getSeatId(x) for x in input)  # 888
minSeatId = min(getSeatId(x) for x in input)  # 89
mySeatId = list(set(list((getSeatId(x) for x in input))) ^ set(
    list(range(minSeatId, maxSeatId + 1))))[0]  # 522
# %%
