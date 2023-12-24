from itertools import combinations
stones = [[[int(i) for i in part.split(', ')] for part in line.split(' @ ')] for line in open('input.txt').read().splitlines()]
total = 0
for stone_a, stone_b in combinations(stones, 2):
    try:
        b = (stone_b[0][0] / stone_a[1][0] - stone_a[0][0] / stone_a[1][0] - stone_b[0][1] / stone_a[1][1] + stone_a[0][1] / stone_a[1][1]) / (stone_b[1][1] / stone_a[1][1] - stone_b[1][0] / stone_a[1][0])
    except ZeroDivisionError:
        continue
    x = stone_b[0][0] + stone_b[1][0] * b
    y = stone_b[0][1] + stone_b[1][1] * b
    if (stone_b[1][0] > 0 and x < stone_b[0][0]) or (stone_b[1][0] < 0 and x > stone_b[0][0]) or (stone_b[1][1] > 0 and y < stone_b[0][1]) or (stone_b[1][1] < 0 and y > stone_b[0][1]):
        continue
    if (stone_a[1][0] > 0 and x < stone_a[0][0]) or (stone_a[1][0] < 0 and x > stone_a[0][0]) or (stone_a[1][1] > 0 and y < stone_a[0][1]) or (stone_a[1][1] < 0 and y > stone_a[0][1]):
        continue
    if x < 200000000000000 or x > 400000000000000 or y < 200000000000000 or y > 400000000000000:
        continue
    total += 1
print(total)
