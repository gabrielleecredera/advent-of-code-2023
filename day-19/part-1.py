import re

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

total = 0
for part in parts.splitlines():
    part = list(map(int, re.findall(r'-?\d+', part)))
    cur_workflow = 'in'
    while True:
        if cur_workflow == 'A':
            total += sum(part)
            break
        elif cur_workflow == 'R':
            break
        for rule in workflows[cur_workflow]:
            if type(rule) is str:
                cur_workflow = rule
                break
            else:
                component, compare, num, target = rule
                component_num = part['xmas'.index(component)]
                if compare == '<':
                    if component_num < num:
                        cur_workflow = target
                        break
                elif compare == '>':
                    if component_num > num:
                        cur_workflow = target
                        break
                else:
                    print('uh oh')
                    exit()
print(total)
