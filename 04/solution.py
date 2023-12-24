# getting relevant string slices
with open("input.txt", 'r') as f:
    lines = [x.strip().split(':')[1].split('|') for x in f.readlines()]

count = 0 # winning numbers

# record for copies of each card, initialized with all 1s for original cards
card_counts = {x+1: 1 for x in range(len(lines))}

# count of "original cards" (lol this problem was pretty vague), i.e., cards which had any winning numbers in our set
original_count = 0

for i, line in enumerate(lines, start=1):
    # two sets of numbers
    winning = [int(x) for x in line[0].strip().split(' ') if x != '']
    ns = [int(x) for x in line[1].strip().split(' ') if x != '']

    # intersection of numbers to find which winning numbers we have, length of that intersection
    intersection = set(winning) & set(ns)
    l = len(intersection)

    if l:
        # part 1
        count += 2**(l-1)

        # part 2
        original_count += 1
        for x in range(i+1, i+1+l):
            card_counts[x] += card_counts[i]

print(count)
print(
        sum( [card_counts[x+1] for x in range(len(lines)) ])
    )
        

