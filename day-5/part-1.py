import re

input = open('input.txt').read()
seeds = list(map(int, re.findall(r'(\d+)', input.split('\n\n')[0])))
lowest_num = 999999999999999999
for seed in seeds:
    latest_num = seed
    for group in input.split('\n\n')[1:]:
        found_mapping = False
        for mapping in group.split('\n')[1:]:
            if not mapping:
                continue
            mapping = list(map(int, re.findall(r'(\d+)', mapping)))
            if mapping[1] <= latest_num < mapping[1] + mapping[2]:
                latest_num = mapping[0] + (latest_num - mapping[1])
                found_mapping = True
                break
    lowest_num = min(lowest_num, latest_num)
print(lowest_num)
