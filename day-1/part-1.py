import re

input = open('input.txt').read()
print(sum([int(pair[0] + (pair[0] if pair[1] == '' else pair[1])) for pair in re.findall(r'.*?(\d)(?:.*(\d)|).*', input)]))
