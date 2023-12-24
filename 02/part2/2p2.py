lines = []

with open("input.txt", "r") as f:
    lines = f.readlines()

max_val = {
        "red": 12,
        "green": 13,
        "blue": 14
}


sum = 0

rows = []
for gameid, line in enumerate(lines, start=1):
    throws = [l.strip() for l in line.split(':')[1].replace(';',',').split(',')]
    throws = [{t.split(' ')[1] : int(t.split(' ')[0])} for t in throws]
    print(line)
    print(throws)

    power = 1

    invalidgame = False
    for color in ["red", "green", "blue"]:
        occurrences = list(filter(lambda x: color in x, throws))
        values = [x[color] for x in occurrences]
        
        if max(values) > max_val[color]:
            invalidgame = True
            break

        print(color, values, "->", min(values))
        power *= min(values)

    if not invalidgame:
        sum += power

print(sum)

