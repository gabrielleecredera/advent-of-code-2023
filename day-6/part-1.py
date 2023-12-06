import math
import re

times = re.findall(r'(\d+)', open('input.txt').read().split('\n')[0])
distances = re.findall(r'(\d+)', open('input.txt').read().split('\n')[1])
total = 1

for race in range(0, len(times)):
    a = -1
    b = int(times[race])
    c = int(distances[race]) * -1
    pt1, pt2 = sorted([(-1 * b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a), (-1 * b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)])
    total *= math.floor(pt2) - math.ceil(pt1) + 1
print(total)
