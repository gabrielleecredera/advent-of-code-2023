print('diagraph {')
for line in open('input.txt').read().splitlines():
    a, b = line.split(': ')
    print(a, '->', ', '.join(b.split(' ')))
print('}')
