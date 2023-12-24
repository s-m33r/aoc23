with open("input.txt", 'r') as f:
    count = 0
    for line in [x.strip().split(':')[1] for x in f.readlines()]:
        line = line.split('|')

        winning = [int(x) for x in line[0].strip().split(' ') if x != '']
        ns = [int(x) for x in line[1].strip().split(' ') if x != '']

        intersection = set(winning) & set(ns)
        l = len(intersection)

        count += 2**(l-1) if l else 0

print(count)
        

