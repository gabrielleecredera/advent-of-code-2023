from queue import Queue
import json

states = {}
for line in open('input.txt').read().splitlines():
    from_mod, to_mod = line.split('->')
    mod_type = from_mod[0]
    name = from_mod.strip() if mod_type == 'b' else from_mod[1:].strip()
    dests = [i.strip() for i in to_mod.split(',')]
    if mod_type == 'b':
        state = None
    elif mod_type == '%':
        state = False
    elif mod_type == '&':
        state = {}
    states[name] = {
        'type': mod_type,
        'state': state,
        'dests': dests,
    }
for name in [state for state in states if states[state]['type'] == '&']:
    states[name]['state'] = {state: False for state in states if name in states[state]['dests']}

signals = Queue()
counts = { True: 0, False: 0 }
i = 0
while True:
    i += 1
    signals.put(('button', False, 'broadcaster'))
    while signals.qsize():
        from_mod, signal, to_mod = signals.get()
        counts[signal] += 1
        if to_mod not in states:
            continue
        state = states[to_mod]
        if state['type'] == 'b':
            list(map(signals.put, [(to_mod, signal, dest) for dest in state['dests']]))
        elif state['type'] == '%':
            if not signal:
                state['state'] = not state['state']
                list(map(signals.put, [(to_mod, state['state'], dest) for dest in state['dests']]))
        elif state['type'] == '&':
            state['state'][from_mod] = signal
            out_signal = not all(state['state'].values())
            list(map(signals.put, [(to_mod, out_signal, dest) for dest in state['dests']]))
    if i == 1000:
        break
print(counts[True] * counts[False])
            