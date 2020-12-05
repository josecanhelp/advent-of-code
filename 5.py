input = list(open("input-day5.txt", "r"))


def splitTicket(line):
    return {
        'row': line[0:7].replace("F", "0").replace("B", "1"),
        'col': line[-4::].replace("\n", "").replace("R", "1").replace("L", "0")
    }


def getSeatId(line):
    return int(splitTicket(line)['row'], 2) * 8 + int(splitTicket(line)['col'], 2)


maxSeatId = max(getSeatId(x) for x in input)  # 888
minSeatId = min(getSeatId(x) for x in input)  # 89
mySeatId = list(set(list((getSeatId(x) for x in input))) ^ set(
    list(range(minSeatId, maxSeatId + 1))))[0]  # 522
