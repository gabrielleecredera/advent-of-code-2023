import re
import itertools
import functools

@functools.lru_cache(maxsize=None)
def step(record, sizes):
    next_unknown = record.find('?')
    if next_unknown == -1:
        matches = tuple([len(i) for i in re.findall(r'(#+)(?:\.|$)', record)])
        if matches == sizes:
            return 1
        else:
            return 0
    else:
        matches = tuple([len(i) for i in re.findall(r'(#+)\.', record[:next_unknown + 1])])
        if matches != sizes[:len(matches)]:
            return 0
        if record.count('?') + record.count('#') < sum(sizes):
            return 0
        prev_gap = record.rfind('.', 0, next_unknown)
        count_a = step(record[prev_gap + 1:next_unknown] + '.' + record[next_unknown + 1:], sizes[len(matches):])
        count_b = step(record[prev_gap + 1:next_unknown] + '#' + record[next_unknown + 1:], sizes[len(matches):])
        return  count_a + count_b

total = 0
for line in open('input.txt'):
    record = '?'.join([line.split(' ')[0]] * 5)
    sizes = tuple(map(int, line.split(' ')[1].split(','))) * 5
    count = step(record, sizes)
    total += count
print(total)
