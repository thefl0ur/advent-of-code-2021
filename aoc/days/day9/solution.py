from typing import List, Tuple


Matrix = List[List[int]]
Coordinate = Tuple[int, int]


def read_data(file_name) -> Matrix:
    with open(file_name, 'r') as file:
        return [list(map(int, list(line.strip()))) for line in file]


def part1(file_path: str) -> int:
    heatmap = Heatmap(read_data(file_path))
    return heatmap.get_risk_lever()


def part2(file_path: str) -> int:
    heatmap = Heatmap(read_data(file_path))
    heatmap.get_basins()

    prod = 1
    for x in sorted(heatmap.basins)[-3:]:
        prod = prod * x

    return prod


class Heatmap:

    def __init__(self, matrix) -> None:
        self.low_points = []
        self.basins = []
        self.matrix = matrix

    def is_lower(self, current: int, adjacents: List[int]) -> bool:
        for x in adjacents:
            if current > x:
                return False
        return True

    def _get_lowest_points(self) -> None:
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

    def get_risk_lever(self) -> int:
        self._get_lowest_points()
        risk_level = 0
        for x, y in self.low_points:
            risk_level += self.matrix[x][y] + 1

        return risk_level

    def get_basins(self) -> None:
        self._get_lowest_points()
        for x, y in self.low_points:
            stack = []
            self.flood((x, y), stack)
            self.basins.append(len(stack))

    def flood(self, position: Coordinate, stack: List[Coordinate]) -> None:
        x, y = position

        if x < 0 or y < 0:
            return

        try:
            if self.matrix[x][y] == 9:
                return
        except IndexError:
            return

        # check is position already visited
        if position in stack:
            return

        stack.append(position)
        self.flood((x, y+1), stack)
        self.flood((x+1, y), stack)
        self.flood((x, y-1), stack)
        self.flood((x-1, y), stack)
