total = 0
for pattern_raw in open('input.txt').read().split('\n\n'):
    pattern = pattern_raw.splitlines()
    for y in range(1, len(pattern)):
        max_rows = min(y, len(pattern) - y)
        up = ''.join(pattern[(y - 1) - max_rows + 1:y][::-1])
        down = ''.join(pattern[y:y + max_rows])
        one_diff = None
        for i in range(len(up)):
            if up[i] != down[i]:
                if one_diff == True:
                    one_diff = False
                    break
                elif one_diff == None:
                    one_diff = True
        if one_diff == True:
            total += 100 * y
            break
    for x in range(1, len(pattern[0])):
        one_diff = None
        for row in pattern:
            max_cols = min(x, len(pattern[0]) - x)
            left = ''.join(row[(x - 1) - max_cols + 1:x][::-1])
            right = ''.join(row[x:x + max_cols])
            for i in range(len(left)):
                if left[i] != right[i]:
                    if one_diff == True:
                        one_diff = False
                        break
                    elif one_diff == None:
                        one_diff = True
            if one_diff == False:
                break
        if one_diff == True:
            total += x
            break
print(total)
