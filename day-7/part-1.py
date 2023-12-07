import collections

def get_hand_strength(hand: list[str]) -> int:
    counter = collections.Counter(hand)
    if 5 in counter.values():
        return 7
    if 4 in counter.values():
        return 6
    if 3 in counter.values() and 2 in counter.values():
        return 5
    if 3 in counter.values() and 1 in counter.values():
        return 4
    if list(counter.values()).count(2) == 2:
        return 3
    if 2 in counter.values() and list(counter.values()).count(1) == 3:
        return 2
    if list(counter.values()).count(1) == 5:
        return 1

def get_adjusted_hand_strength(hand: list[str]) -> int:
    strength = get_hand_strength(hand)
    strength_key = '23456789TJQKA'
    for char in hand:
        strength = strength * 100 + strength_key.index(char)
    return strength

total = 0
order = sorted([(line[0:5], int(line[5:])) for line in open('input.txt')], key=lambda pair: get_adjusted_hand_strength(pair[0]))
for i, pair in enumerate(order):
    total += (i + 1) * pair[1]
print(total)
