import math
import re

time = int(''.join(re.findall(r'(\d+)', open('input.txt').read().split('\n')[0])))
distance = int(''.join(re.findall(r'(\d+)', open('input.txt').read().split('\n')[1])))

a = -1
b = time
c = distance * -1
pt1, pt2 = sorted([(-1 * b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a), (-1 * b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)])
print(math.floor(pt2) - math.ceil(pt1) + 1)
