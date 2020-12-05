# %%
input = open("input-day5.txt", "r")
# %%


def getSeatId(line):
    rowBin = line[0:7].replace("F", "0").replace("B", "1")
    colBin = line[-3::].replace("R", "1").replace("L", "0")
    row = int(rowBin, 2)
    col = int(colBin, 2)
    seatId = int(rowBin, 2) * 8 + int(colBin, 2)
    return seatId


# %%
print(max(getSeatId(x) for x in input))  # 888
# %%
