sum = 0

with open("1_input.txt", 'r') as inp:
    for line in inp.readlines():

        l = list(
            filter(lambda x: x.isnumeric(), line)
        )

        sum += 10 * int(l[0]) + int(l[-1])

print(sum)
