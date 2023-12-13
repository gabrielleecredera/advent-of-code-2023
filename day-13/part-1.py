total = 0
for pattern_raw in open('input.txt').read().split('\n\n'):
    pattern = pattern_raw.splitlines()
    for y in range(1, len(pattern)):
        max_rows = min(y, len(pattern) - y)
        if pattern[(y - 1) - max_rows + 1:y][::-1] == pattern[y:y + max_rows]:
            total += 100 * y
            break
    for x in range(1, len(pattern[0])):
        match = True
        for row in pattern:
            max_cols = min(x, len(pattern[0]) - x)
            if row[(x - 1) - max_cols + 1:x][::-1] != row[x:x + max_cols]:
                match = False
                break
        if match:
            total += x
            break
print(total)
