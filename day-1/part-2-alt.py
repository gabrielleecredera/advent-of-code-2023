import re

numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
input = open('input.txt').read()
matches = re.findall(r'.*?(\d|one|two|three|four|five|six|seven|eight|nine)(?:.*(\d|one|two|three|four|five|six|seven|eight|nine)|).*', input)
pairs = [([str(numbers.index(match[0]) + 1) if match[0] in numbers else match[0], str(numbers.index(match[1]) + 1) if match[1] in numbers else match[1]]) for match in matches]
print(sum([int(pair[0] + (pair[0] if pair[1] == '' else pair[1])) for pair in pairs]))
