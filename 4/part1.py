from typing import List

def read_data(file_name: str) -> List[str]:
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            data.append(line.rstrip())
    return data


data = read_data('data/test_input.in')
game_input = list(map(int, data[0].split(',')))
fields= []
count = 0

for line in data[1:]:
    if (line.rstrip() != ''):
        count += 1      
        fields[-1].append(list(map(int, line.split())))
    else:
        fields.append([])
        count = 0

def do_step(input_value):
    for field in fields:
        # по строкам
        for i in range(len(field[0])):
            # по столбам
            for j in range(len(field)):
                if field[i][j] == input_value:
                    field[i][j] = 'X'

def check_winners():
    for field in fields:
       # по строкам
        for line in field:
            # import pdb; pdb.set_trace()
            if all(x == 'X' for x in line):
                return True, field
    
    #rotate
    rotated = []
    for field in fields:
        data = [[0 for x in range(5)] for y in range(5)]
        current_col = 0
        for line in field:
            for index in range(len(line)):
                data[index][current_col] = line[index]
            current_col += 1
        rotated.append(data)

    index_ = 0
    for field in rotated:
       # по строкам
        for line in field:
            # import pdb; pdb.set_trace()
            if all(x == 'X' for x in line):
                return True, fields[index_]
        index_ += 1

    return False, None   

# wait_till_win = False
# for _input in game_input:
#     do_step(_input)
#     have, winner = check_winners()
    
#     # print(len(fields))
#     if have and len(fields) >= 2:
        
#         fields.remove(winner)
        
#         if (len(fields)) == 1:
            
#             wait_till_win = True
#             continue

#     if wait_till_win and have:
#         summ = 0
#         for line in range(len(fields[0])):
#             for col in range(len(fields[0])):
#                 if isinstance(fields[0][line][col], int):
#                     summ += fields[0][line][col]

#         print(summ*_input)
#         break
    
#     # part 1
#     # if not have:
#     #     continue

#     # summ = 0
#     # for line in range(len(winner[0])):
#     #     # import pdb; pdb.set_trace()
#     #     for col in range(len(winner)):
#     #         if isinstance(winner[line][col], int):
#     #             summ += winner[line][col]

#     # print(summ*_input)
#     # break
