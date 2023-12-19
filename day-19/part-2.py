import re
import math

workflows_raw, parts = open('input.txt').read().split('\n\n')
workflows = {}
for workflow in workflows_raw.splitlines():
    name, rest = workflow.split('{')
    rules = []
    for rule in rest[:-1].split(','):
        matches = re.match(r'(.*)([<>])(-?.*):(.*)', rule)
        if matches is not None:
            groups = matches.groups()
            rules.append((groups[0], groups[1], int(groups[2]), groups[3]))
        else:
            rules.append(rule)
        workflows[name] = rules

def get_combinations(cur_workflow, ranges):
    if cur_workflow == 'A':
        return math.prod([range[1] - range[0] + 1 for range in ranges])
    elif cur_workflow == 'R':
        return 0
    step_total = 0
    remaining_ranges = ranges
    for rule in workflows[cur_workflow]:
        if type(rule) is str:
            step_total += get_combinations(rule, remaining_ranges)
            break
        else:
            component, compare, num, target = rule
            component_index = 'xmas'.index(component)
            if compare == '<':
                if remaining_ranges[component_index][0] < num:
                    step_total += get_combinations(target, [(range[0], num - 1) if i == component_index else range for i, range in enumerate(remaining_ranges)])
                    remaining_ranges = [(num, range[1]) if i == component_index else range for i, range in enumerate(remaining_ranges)]
            elif compare == '>':
                if remaining_ranges[component_index][1] > num:
                    step_total += get_combinations(target, [(num + 1, range[1]) if i == component_index else range for i, range in enumerate(remaining_ranges)])
                    remaining_ranges = [(range[0], num) if i == component_index else range for i, range in enumerate(remaining_ranges)]
            else:
                print('uh oh')
                exit()
    return step_total


print(get_combinations('in', [(1, 4000)] * 4))
