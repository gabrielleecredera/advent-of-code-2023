total = 0
for line in open('input.txt').read().splitlines():
    win = [x for x in line.split(':')[1].split('|')[0].strip().split(' ') if x]
    have = [x for x in line.split('|')[1].strip().split(' ') if x]
    have_win = len([x for x in have if x in win])
    if have_win == 0:
        continue
    total += 2 ** (have_win - 1)
print(total)
