def read_data(file_name):
    with open(file_name, 'r') as file:
        data = []
        for line in file:
            data.append(list(map(int, [x for x in line.strip()])))
        return data

data = read_data('data/input.in')

def find_low_points(matrix):
    summ = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            adj = []
            if x > 0:
                adj.append(matrix[x-1][y])
            if x < len(matrix)-1:
                adj.append(matrix[x+1][y])
            
            if y > 0:
                adj.append(matrix[x][y-1])
            if y < len(matrix[0])-1:
                adj.append(matrix[x][y+1])

            current = matrix[x][y]
            if all(current < xx for xx in adj):
                print(f"cur: {current} adj: {adj}")
                summ += current + 1

    return summ

points = find_low_points(data)

if points != 15:
    print('failed')

print(points)