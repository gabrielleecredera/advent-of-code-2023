import itertools

directions = [0 if i  == 'L' else 1 for i in open('input.txt').read().split('\n')[0]]
map = {}
for line in open('input.txt').read().split('\n')[2:]:
    if not line:
        continue
    map[line[0:3]] = (line[7:10], line[12:15])

count = 0
location = 'AAA'
for direction in itertools.cycle(directions):
    count += 1
    location = map[location][direction]
    if location == 'ZZZ':
        print(count)
        exit()
