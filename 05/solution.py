class Map:
    def __init__(self, maps):
        self.ranges = []

        for item in maps:
            dst_start = item[0]
            src_start = item[1]
            length = item[2]

            self.ranges.append(
                    (src_start, src_start+length-1,
                     dst_start, dst_start+length-1)
            )

    def getMapped(self, x):
        for rng in self.ranges:
            if rng[0] <= x and x <= rng[1]:

                y = rng[2] + (x - rng[0])
                if y <= rng[3]:
                    return y

        return x

with open("input.txt", "r") as f:
    lines = f.read().split('\n\n')

# seeds
seeds = [int(n) for n in lines[0].split(':')[1].strip().split(' ')]

# creating maps
maps_list = []
for _, data in [(l.split(':')[0],l.split(':')[1]) for l in lines[1:]]:
    data = [[int(n) for n in x.strip().split(' ')] for x in data.split('\n') if x != '']
    maps_list.append(Map(data))

def min_loc(seed):
    x = seed
    for m in maps_list:
        x = m.getMapped(x)

    return x

# getting values by descending down the list of maps
def min_loc_for_seeds(first, seeds):
    minloc = min_loc(first)

    for seed in seeds:
        y = min_loc(seed)
        minloc = y if y < minloc else minloc
    
    return minloc

# print minimum location
print("part 1:", min_loc_for_seeds(seeds[0], seeds))

# part 2, treating seeds as range pairs
print("NOTE: part 2 took 38 minutes to compute on my PC ;P")

seeds_itr = []
for i in range(0, len(seeds), 2):
    seeds_itr.append(
        (seeds[i], seeds[i+1])
    )

minloc = min_loc(seeds[0])
for x1, x2 in seeds_itr:
    y = min_loc_for_seeds(x1, iter(range(x1, x1+x2-1)))
    minloc = y if y < minloc else minloc

print("part 2:", minloc)

