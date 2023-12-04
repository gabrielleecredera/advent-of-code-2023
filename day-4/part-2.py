from collections import defaultdict

total = defaultdict(lambda: 1)
for i, line in enumerate(open('input.txt').read().splitlines()):
    win = [x for x in line.split(':')[1].split('|')[0].strip().split(' ') if x]
    have = [x for x in line.split('|')[1].strip().split(' ') if x]
    have_win = len([x for x in have if x in win])
    if have_win == 0:
        continue
    for j in range(have_win):
        total[i + 1 + j + 1] += 1 * total[i + 1]

score = 0
for i in range(1, len(open('input.txt').read().splitlines()) + 1):
    score += total[i]
print(score)
