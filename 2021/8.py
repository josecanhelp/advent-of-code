# %%
from parse import findall, search
from collections import Counter


def lineToTuple(line):
    return (search('{action:w} {value:d}', line))


def accumulator(line, idx, accum):
    acc = acc + line['value']
    memory.append(idx)
    callAction(bootcode[idx + 1], idx, accum)


def jump(line, idx, accum):
    memory.append(idx)
    callAction(bootcode[idx + line['value']], idx, accum),


def nope(line, idx, accum):
    memory.append(idx)
    callAction(bootcode[idx + 1], idx, accum),


def callAction(line, idx, accum):
    switcher = {
        'acc': accumulator(line, idx, accum),
        'jmp': jump(line, idx, accum),
        'nop': nope(line, idx, accum)
    }

    return switcher.get(line['action'])(line, idx, accum) if flag else print(acc)


def main():
    memory = [0]
    acc = 0
    flag = 0
    bootcode = [lineToTuple(x) for x in open('test.txt')]
    callAction(bootcode[0], 0, 0)
