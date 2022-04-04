from collections import defaultdict

def read_data(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def parce(data):
    separator_finded = False
    template = ''
    replacements = {}

    for line in data:
        if line == '':
            separator_finded = True
            continue

        if not separator_finded:
            template = line
        else:
            k, v = line.split(' -> ')
            replacements[k] = v

    return (template, replacements)

def generate(pairs, rules, cntr):
    result = defaultdict(int)
    for pair, num in pairs.items():
        new_element = rules[pair]
        cntr[new_element] += num

        result[f'{pair[0]}{new_element}'] += num
        result[f'{new_element}{pair[1]}'] += num
    

    return result, cntr

data = read_data('data/input.in')
base_template, replacements = parce(data)
pairs = defaultdict(int)

index = 0
while index < len(base_template) -1:
    pairs[base_template[index:index+2]] = 1
    letter1 = base_template[index:index+1]
    index += 1

steps = 10
from collections import Counter
cntr = Counter(base_template)

for _step in range(steps):
    print(_step)
    pairs, cntr = generate(pairs, replacements, cntr)
    
items = cntr.most_common()
print(items)
print(items[0][1] - items[-1][1])
