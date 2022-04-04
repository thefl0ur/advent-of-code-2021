def read(path):
    data = []
    with open(path) as f:
        for line in f:
            data.append(line.rstrip())
    return data

print(sum(sum([1 if len(x) in [3, 4, 2, 7] else 0 for x in [x.strip() for x in line.split('|')[1].strip().split(' ')]]) for line in read('data/input.in')))
