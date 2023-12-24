import re

with open("input.txt", 'r') as f:
    lines = [x.strip() for x in f.readlines()]

WIDTH, HEIGHT = len(lines[0]), len(lines)

# get co-ordinates of all non-'.' symbols
symbols = []
for linum, line in enumerate(lines):
    matches = list(re.finditer("[^.0-9]+", line))
    if matches != []:
        symbols.append(
                (linum, [x.start() for x in matches])
            )

numbers = []
gear_ratios = []
for y, xs in symbols:
    ninline = list(re.finditer("[0-9]+", lines[y]))

    nupper, nlower = None, None
    try: nupper = list(re.finditer("[0-9]+", lines[y-1]))
    except IndexError: pass

    try: nlower = list(re.finditer("[0-9]+", lines[y+1]))
    except IndexError: pass

    nvertical = nupper + nlower if nupper and nlower else None

    for x in xs:
        entry = []

        # horizontally adjacent part numbers
        entry += [int(n.group(0)) for n in ninline if (n.span()[0] == x+1) or (n.span()[1] == x)]

        # vertically adjacent part numbers (also diagonal)
        if nvertical:
            entry += [int(n.group(0)) for n in nvertical if (n.span()[0] in (x-1,x,x+1)) or (n.span()[1] - 1 in (x-1,x,x+1)) or (x < n.span()[1] and x >= n.span()[0]) ]

        # appending gear ratio if part is a gear
        if len(entry) == 2:
            gear_ratios.append(entry[0] * entry[1])

        # appending part numbers
        numbers += entry

print("sum of all part numbers: ", sum(numbers))
print("sum of gear ratios: ", sum(gear_ratios))
