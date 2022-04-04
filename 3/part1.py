from typing import List

def read_data(file_name: str) -> List[str]:
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            data.append(line.rstrip())
    return data

def transform(input_data):
    row_count = len(input_data[0])
    col_count = len(input_data)

    data = [[0 for x in range(col_count)] for y in range(row_count)]

    current_col = 0
    for line in input_data:
        for index in range(len(line)):
            data[index][current_col] = int(line[index])
        current_col += 1

    return data
        
def calc_part1(data) -> int:
    size = len(data[0])
    base_gamma = []
    base_eps = []
    for line in data:
        tmp = sum(line)
        if tmp > size/2:
            base_gamma.append("1")
            base_eps.append("0")
        else:
            base_gamma.append("0")
            base_eps.append("1")

    gamma = int('0b' + ''.join(base_gamma), 2)
    epsilon = int('0b' + ''.join(base_eps), 2)
    return gamma * epsilon

original_data = read_data('data/input.in')
transofrmed_data = transform(original_data)
result = calc_part1(transofrmed_data)
# if result != 198:
#     print('failed')
print(result)

def get_most_common_in_line(line):
    return 1 if sum(line) >= (len(line)/2) else 0

def column(matrix, i):
    return [row[i] for row in matrix]

def get_all_columns(data, index, most_common):
    indexes = []
    for i in range(len(data[index])):
        if data[index][i] == most_common:
            indexes.append(i)
    
    tmp = []
    for i in range(len(indexes)):
        tmp.append(column(data, indexes[i]))
    
    size = len(tmp[0])
    new_data = [[0 for x in range(len(tmp))] for y in range(size)]
    
    col = 0
    for line in tmp:
        for i in range(len(line)):
            new_data[i][col] = line[i]
        col += 1

    return new_data

def process(data, index = 0, most_common = True):
    # import pdb; pdb.set_trace()
    if len(data[0]) == 1:
        return data

    most_common_value = get_most_common_in_line(data[index])
    if not most_common:
        most_common_value = int(not bool(most_common_value))
    temp_data = get_all_columns(data, index, most_common_value)
    index += 1
    return process(temp_data, index, most_common)


data = process(transofrmed_data)
data1 = process(data=transofrmed_data, most_common=False)
string = "0b"
string1 = "0b"
for line in data:
    string += str(line[0])

for line in data1:
    string1 += str(line[0])

oxy = int(string, 2)
co2 = int(string1, 2)

print(f"{oxy} * {co2} = {oxy * co2}")