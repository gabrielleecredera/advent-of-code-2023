sequence = open('input.txt').read().split(',')
total = 0
for text in sequence:
    value = 0
    for char in text.strip():
        value += ord(char)
        value *= 17
        value %= 256
    total += value
print(total)
