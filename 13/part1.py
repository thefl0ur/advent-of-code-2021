def parce_data():
    raw_data = None
    with open('data/input.in') as f:
        raw_data = [line.strip() for line in f.readlines()]

    points = []
    foldings = []
    separator_finded = False
    for data in raw_data:
        if data == '':
            separator_finded = True
            continue

        if not separator_finded:
            points.append(tuple(map(int, data.split(','))))
        else:
            fold_coord = data.split('fold along ')[1].split('=')
            foldings.append((fold_coord[0], int(fold_coord[1])))

    return points, foldings 

def build_matrix(data):
    max_x = max([x[0] for x in data])
    max_y = max([x[1] for x in data])
    matrix =  [[0 for x in range(max_x+1)] for y in range(max_y+1)]

    for point in data:
        x, y = point
        print(f'{x}, {y}')
        matrix[y][x] = '#'
    
    return matrix

def print_matrix(matrix):
    for x in range(len(matrix)):
        string = ""
        for y in range(len(matrix[0])):
            if matrix[x][y] != '#':
                string += ' .'
            else:
                string += ' #'
        print(string)

def fold(matrix, fold):
    orientation, position = fold

    if orientation == 'x':
        # print('--------------------')
        # print_matrix(matrix)
        sub1 = [[0 for y in range(position)] for x in range(len(matrix))]
        sub2 = [[0 for y in range(position)] for x in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if col < position:
                    sub1[row][col] = matrix[row][col]
                if col > position:
                    sub2[row][col - position - 1] =  matrix[row][col]
        
        for row in range(len(sub2)):
            for col in range(len(sub2[0])):
                if sub2[row][col] == '#':
                    sub1[row][len(sub2[0]) - col - 1] = "#"
        return(sub1)
    else:
        sub1 = matrix[0:position]
        sub2 = matrix[position+1:]

        for row in range(len(sub2)):
            for col in range(len(sub2[0])):
                if sub2[row][col] == '#':
                    sub1[len(sub2) - row - 1][col] = "#"

    return sub1

points, foldings = parce_data()
print(points)
print(foldings)

matrix = build_matrix(points)
# folded = fold(matrix, foldings[0])
# summ = 0
# for line in folded:
#     summ += sum([1 for x in line if x == '#'])
# print(summ)

for instr in foldings:
    matrix = fold(matrix, instr)

print_matrix(matrix)