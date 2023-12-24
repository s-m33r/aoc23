with open("input.txt", 'r') as f:
    lines = [[ y for y in x.split(':')[1].strip().split(' ') if y != ''] for x in f.read().split('\n') if x != '']
    data = dict(zip(lines[0], lines[1]))

def waysToWin(n, y):
    ways = 0
    for x in range(1, n):
        if x*(n-x) > y:
            ways += 1
    return ways
    
res = 1
for n in data:
    ways = waysToWin(int(n), int(data[n]))
    res *= ways

print(res)

X = int(''.join(lines[0]))
Y = int(''.join(lines[1]))
print(waysToWin(X, Y))
