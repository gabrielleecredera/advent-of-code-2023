from typing import Tuple

total = 0
lines = open('input.txt').read().splitlines()

def read_num_at_pos(pos: Tuple[int, int]) -> int:
    start_pos = 0
    end_pos = len(lines[pos[0]]) - 1
    for col in range(pos[1], -1, -1):
        if not lines[pos[0]][col].isdecimal():
            start_pos = col + 1
            break
    for col in range(pos[1], len(lines[pos[0]])):
        if not lines[pos[0]][col].isdecimal():
            end_pos = col - 1
            break
    return int(lines[pos[0]][start_pos:end_pos + 1])

for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char == '*':
            raw_digit_pos = []
            start_row = max(row - 1, 0)
            end_row = min(row + 1, len(lines) - 1)
            start_col = max(col - 1, 0)
            end_col = min(col + 1, len(line) - 1)
            for i in range(start_row, end_row + 1):
                for j in range(start_col, end_col + 1):
                    if lines[i][j].isdecimal():
                        raw_digit_pos.append((i, j))
            digit_pos = []
            for pos in raw_digit_pos:
                if not (pos[0], pos[1] - 1) in raw_digit_pos:
                    digit_pos.append(pos)
            if len(digit_pos) != 2:
                continue
            total += read_num_at_pos(digit_pos[0]) * read_num_at_pos(digit_pos[1])
print(total)
