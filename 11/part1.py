def read_data(filename):
    data = []
    with open(filename, 'r') as file:
        data = [[int(num) for num in line.strip()] for line in file]
    return data

def print_data(matrix):
    for i in range(len(matrix)):
        string = ""
        for j in range(len(matrix[0])):
            string += " " + str(matrix[i][j])
        
        print(string)

data = read_data('data/input.in')
# print_data(data)

steps_count = 1000
blinks = 0

for step in range(steps_count):
    stack = []

    if sum(map(sum, data)) == 0:
        print(f"break step = {step}")
        break;

    for row in range(len(data)):
        for col in range(len(data[0])):
            data[row][col] += 1

            if data[row][col] >= 9:
                stack.append((row, col))

    while len(stack) > 0:
        row, col = stack.pop(0)
        # breakpoint()
        if data[row][col] > 9:
            blinks += 1
            data[row][col] = 0

            data_range = [-1, 0, 1]

            neighbors = []
            for x in data_range:
                for y in data_range:
                    dx = row + x
                    dy = col + y

                    if (dx >= 0 and dx < len(data)) and (dy >= 0 and dy < len(data[0])):
                        neighbors.append((dx, dy))

            # breakpoint()
            for neighbor in neighbors:
                nx, ny = neighbor
                if data[nx][ny] != 0:
                    data[nx][ny] += 1

                if data[nx][ny] > 9:
                    stack.append((nx, ny))

    # print(f'After step {step+1}:')
    # print_data(data)

print(blinks)