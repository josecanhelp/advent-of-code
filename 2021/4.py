# %%
import itertools
import math
import re

input = open("input-day4.txt", "r")

def removeNewline(el):
   return el.replace('\n', '')

def toTuple(st):
    return (tuple(st.split(":")))

def group(seq, sep):
    g = []
    for el in seq:
        if el == sep:
            yield g
            g = []
        if el != sep:
            g.append(removeNewline(el))
    yield g

result = list(group(input, '\n'))
new = list((x.split(" ") for x in list((" ".join(x) for x in result))))
p = []

for x in new:
    q = []
    for n in x:
        q.append(toTuple(n))

    p.append(q)

v = (dict(x) for x in p)
# %%

def validation(passport):
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    diff = set(list(passport.keys())) ^ set(required)
    return furtherValidation(passport) if(diff == {'cid'} or diff == set()) else 0

def heightValidation(height):
    matches = re.search(r"(?P<units>\d+)(?P<unit>cm|in)", height)
    if(matches != None):
        if(matches["unit"] == "cm"):
            return 1 if 150 <= int(matches["units"]) <= 193 else 0
        elif (matches["unit"] == "in"):
            return 1 if 59 <= int(matches["units"]) <= 76 else 0
        else:
            return 0
    else:
        return 0

def hairValidation(hair):
    matches = re.search(r"#(?P<color>[0-9a-z]{6}$)", hair)
    return matches != None

def eyeValidation(eye):
    matches = re.search(r"(?P<eyecolor>amb|blu|brn|gry|grn|hzl|oth$)", eye)
    return matches != None

def pidValidation(pid):
    matches = re.search(r"^(?P<iden>\d{9}$)", pid)
    return matches != None

def furtherValidation(passport):
    return 1 if (
        (1920 <= int(passport["byr"]) <= 2002) and
        (2010 <= int(passport["iyr"]) <= 2020) and
        (2020 <= int(passport["eyr"]) <= 2030) and
        heightValidation(passport["hgt"]) and
        hairValidation(passport["hcl"]) and
        eyeValidation(passport["ecl"]) and
        pidValidation(passport["pid"])
     ) else 0

math.fsum(validation(x) for x in v) # 101