import re

def step(record, sizes):
    next_unknown = record.find('?')
    if next_unknown == -1:
        matches = [len(i) for i in re.findall(r'(#+)(?:\.|$)', record)]
        if matches == sizes:
            return 1
        else:
            return 0
    else:
        matches = [len(i) for i in re.findall(r'(#+)\.', record[:next_unknown + 1])]
        if matches != sizes[:len(matches)]:
            return 0
        count_a = step(record[:next_unknown] + '.' + record[next_unknown + 1:], sizes)
        count_b = step(record[:next_unknown] + '#' + record[next_unknown + 1:], sizes)
        return  count_a + count_b

total = 0
for line in open('input.txt'):
    record = line.split(' ')[0]
    sizes = list(map(int, line.split(' ')[1].split(',')))
    count = step(record, sizes)
    total += count
print(total)
