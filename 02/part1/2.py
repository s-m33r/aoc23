with open("input.txt", "r") as f:
    lines = f.readlines()

def invalid_throw(throw):
    for draw in throw:
        color = draw.split(' ')[1]
        count = int(draw.split(' ')[0])
        if {"red": 12, "green": 13, "blue": 14}[color] < count:
            return True

sum = 0

rows = []
for gameid, line in enumerate(lines, start=1):
    flag = False
    throws = [l.split(',') for l in line.split(':')[1].split(';')]

    for throw in throws:
        flag = False
        data = {}
        throw = [x.strip() for x in throw]
        if invalid_throw(throw):
            flag = True
            break
    if flag:
        continue
    sum += gameid

print(sum)
