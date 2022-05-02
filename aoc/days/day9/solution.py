from typing import List, Tuple


Matrix = List[List[int]]
Coordinate = Tuple[int, int]


def read_data(file_name) -> Matrix:
    with open(file_name, 'r') as file:
        data = []
        for line in file:
            data.append(list(map(int, [x for x in line.strip()])))
        return data


def part1(file_path: str) -> int:
    summ = 0
    matrix = read_data(file_path)

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
                summ += current + 1

    return summ


def fill(matrix: Matrix, position: Coordinate, stack: List[Coordinate]) -> None:
    x, y = position

    # map border check
    if x < 0 or x > len(matrix) - 1:
        return
    if y < 0 or y > len(matrix[0]) - 1:
        return

    # basin border check
    if matrix[x][y] == 9:
        return

    # check is position already visited
    if position in stack:
        return
    else:
        stack.append(position)

    fill(matrix, (x, y+1), stack)
    fill(matrix, (x+1, y), stack)
    fill(matrix, (x, y-1), stack)
    fill(matrix, (x-1, y), stack)

    return


def part2(file_path: str) -> int:
    matrix = read_data(file_path)

    lowest_points = []
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
                lowest_points.append((x, y))

    stacks = []
    for x, y in lowest_points:
        stack = []
        fill(matrix, (x, y), stack)
        stacks.append(len(stack))

    stacks.sort()

    prod = stacks[-3]
    for x in stacks[-2:]:
        prod = prod * x

    return prod
