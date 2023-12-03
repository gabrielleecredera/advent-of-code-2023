# this is a BAD solution, should've started from symbols and find the numbers next to them,
# instead of starting from numbers and checking if there are symbols next to them

total = 0
lines = open('input.txt').read().splitlines()
for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char.isdecimal() and (col == 0 or not line[col - 1].isdecimal()):
            num_end_col = False
            for col_b, char_b in enumerate(line[col:]):
                if not char_b.isdecimal():
                    num_end_col = col + col_b - 1
                    break
            if not num_end_col:
                num_end_col = len(line) - 1
            start_row = max(row - 1, 0)
            end_row = min(row + 1, len(lines) - 1)
            start_col = max(col - 1, 0)
            end_col = min(num_end_col + 1, len(line) - 1)
            found_symbol = False
            for i in range(start_row, end_row + 1):
                for j in range(start_col, end_col + 1):
                    if not lines[i][j].isdecimal() and lines[i][j] != '.':
                        found_symbol = True
                        break
                if found_symbol:
                    break
            if found_symbol:
                total += int(line[col:num_end_col + 1])
print(total)
