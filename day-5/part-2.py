import re

input = open('input.txt').read()
ranges = [(int(pair[0]), int(pair[0]) + int(pair[1]) - 1) for pair in re.findall(r'(\d+) (\d+)', input.split('\n\n')[0])]
mappings = [sorted([list(map(int, re.findall(r'(\d+)', mapping))) for mapping in group.split('\n')[1:] if mapping], key=lambda mapping: mapping[1]) for group in input.split('\n\n')[1:] if group.split('\n')[1:]]
for group in mappings:
    new_ranges: list[tuple[int, int]] = []
    for range in ranges:
        found_intersection = False
        for i, mapping in enumerate(group):
            diff = mapping[0] - mapping[1]
            if range[0] < mapping[1] <= range[1] or range[0] <= mapping[1] + mapping[2] - 1 < range[1]:
                found_intersection = True
                intersection_start = max(range[0], mapping[1])
                intersection_end = min(range[1], mapping[1] + mapping[2] - 1)
                new_ranges.append([intersection_start + diff, intersection_end + diff])
                # check space before
                if range[0] < mapping[1] <= range[1]:
                    space_start = max(group[i - 1][1] + group[i - 1][2] - 1 + 1 if i > 0 else 0, range[0])
                    if space_start <= intersection_start - 1:
                        new_ranges.append([space_start, intersection_start - 1])
                # check space after if at end or next one not in same range
                if range[0] <= mapping[1] + mapping[2] - 1 < range[1]:
                    if i == len(group) - 1 or not (range[0] < group[i + 1][1] <= range[1] or range[0] <= group[i + 1][1] + group[i + 1][2] - 1 < range[1]):
                        space_end = min(group[i + 1][1] + group[i + 1][2] - 1 - 1 if i < len(group) - 1 else 999999999999999999999, range[1])
                        if intersection_end + 1 <= space_end:
                            new_ranges.append([intersection_end + 1, space_end])
            elif mapping[1] <= range[0] and mapping[1] + mapping[2] - 1 >= range[1]:
                new_ranges.append([range[0] + diff, range[1] + diff])
                found_intersection = True

        if not found_intersection:
            new_ranges.append(range)

    ranges = new_ranges
print(min([range[0] for range in ranges]))
