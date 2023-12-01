numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
total = 0

for line in open('input.txt'):
    first_num = second_num = None
    for i in range(len(line) - 1):
        if line[i].isdecimal():
            first_num = line[i]
            break
        for j, number in enumerate(numbers):
            if line[i:i + len(number)] == number:
                first_num = str(j + 1)
                break
        if first_num:
            break
    for i in range(len(line) - 2, -1, -1):
        if line[i].isdecimal():
            second_num = line[i]
            break
        for j, number in enumerate(numbers):
            if line[i:i + len(number)] == number:
                second_num = str(j + 1)
                break
        if second_num:
            break
    total += int(first_num + second_num)
print(total)
