from typing import List, Tuple


Matrix = List[List[int]]
Coordinate = Tuple[int, int]


def read_data(file_name) -> Matrix:
    with open(file_name, 'r') as file:
        return [list(map(int, list(line.strip()))) for line in file]


def part1(file_path: str) -> int:
    heatmap = Heatmap(read_data(file_path))
    return heatmap.get_risk_lever()


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


class Heatmap:

    def __init__(self, matrix):
        self.low_points = []
        self.matrix = matrix

    def is_lower(self, current, adjacents):
        for x in adjacents:
            if current > x:
                return False
        return True

    def _get_lowest_points(self):
        for x, _ in enumerate(self.matrix):
            for y, current in enumerate(self.matrix[x]):
                if current == 9:
                    continue

                adjacent_locations = []
                if x > 0:
                    adjacent_locations.append(self.matrix[x-1][y])
                if y > 0:
                    adjacent_locations.append(self.matrix[x][y-1])

                try:
                    adjacent_locations.append(self.matrix[x+1][y])
                except IndexError:
                    pass
                try:
                    adjacent_locations.append(self.matrix[x][y+1])
                except IndexError:
                    pass

                if self.is_lower(current, adjacent_locations):
                    self.low_points.append((x, y))

    def get_risk_lever(self):
        self._get_lowest_points()
        risk_level = 0
        for x, y in self.low_points:
            risk_level += self.matrix[x][y] + 1

        return risk_level
