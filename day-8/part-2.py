import itertools
import math

directions = [0 if i  == 'L' else 1 for i in open('input.txt').read().split('\n')[0]]
map = {}
for line in open('input.txt').read().split('\n')[2:]:
    if not line:
        continue
    map[line[0:3]] = (line[7:10], line[12:15])

locations = [key for key in map.keys() if key[2] == 'A']
loop_lengths = []
for location in locations:
    first_z_position = False
    for i, direction in enumerate(itertools.cycle(directions)):
        if location[2] == 'Z':
            if first_z_position:
                if first_z_position * 2 == i:
                    loop_lengths.append(first_z_position)
                else:
                    print('uh oh')
                    exit()
                break
            else:
                first_z_position = i
        location = map[location][direction]
# at this stage the "bet" that it loops worked
print(math.lcm(*loop_lengths))
