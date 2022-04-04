import copy

def read_date(filename):
    with open(filename) as f:
        return [[char.strip() for char in line] for line in f.readlines()]

def print_map(_map):
    for line in _map:
        print("".join(line))

def step(_data):
    # move >
    data_copy = copy.deepcopy(_data)
    # breakpoint()
    have_move = False
    for row in range(len(_data)):
        for col in range(len(_data[0]) - 1):
            if _data[row][col] in ['.', 'v']:
                continue
            
            # breakpoint()
            next_coord = (row,
            col +1 if (col +1) < len(_data[0]) - 1 else 0)

            if (_data[next_coord[0]][next_coord[1]]) != '.':
                continue
            
            have_move = True
            data_copy[row][col] = '.'
            data_copy[next_coord[0]][next_coord[1]] = '>'

    data_copy1 = copy.deepcopy(data_copy)
    for row in range(len(data_copy)):
        for col in range(len(data_copy[0]) -1 ):
            if data_copy[row][col] in ['.', '>']:
                continue

            next_coord = (
                row +1 if (row +1) < len(data_copy) else 0,
                col)

            if (data_copy[next_coord[0]][next_coord[1]]) != '.':
                continue
            
            have_move = True
            data_copy1[row][col] = '.'
            data_copy1[next_coord[0]][next_coord[1]] = 'v'

    return data_copy1, have_move

data = read_date('data/input.in')
# print_map(data)
# print('#################')
_step = 0
move = True
while move:
    _step += 1
    print(_step)
    data, move = step(data)
print("######")
print(_step)
print("######")