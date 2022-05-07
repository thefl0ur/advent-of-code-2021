from typing import List


def read_data(filename: str) -> List[int]:
    with open(filename, 'r') as file:
        data = [[int(num) for num in line.strip()] for line in file]
    return data


def part1(file_path: str) -> int:
    grid = OctopusGrid(read_data(file_path))

    steps_count = 100
    blinks = 0

    for _ in range(steps_count):
        blinks += grid.step()

    return blinks


def part2(file_path: str) -> int:
    grid = OctopusGrid(read_data(file_path))
    step = 0

    while True:
        grid.step()
        step += 1
        if grid.is_synchronized():
            break

    return step


class OctopusGrid:
    grid_range = [-1, 0, 1]

    def __init__(self, grid: List[int]):
        self.grid = grid
        self.size = len(grid)

    def step(self) -> None:
        blinks = 0
        stack = []

        for row in range(self.size):
            for col in range(self.size):
                self.grid[row][col] += 1

                if self.grid[row][col] >= 9:
                    stack.append((row, col))

        while stack:
            row, col = stack.pop(0)
            if self.grid[row][col] > 9:
                blinks += 1
                self.grid[row][col] = 0

                neighbors = []
                for x in self.grid_range:
                    for y in self.grid_range:
                        dx = row + x
                        dy = col + y

                        if dx >= 0 and dy >= 0:
                            neighbors.append((dx, dy))

                for neighbor in neighbors:
                    nx, ny = neighbor
                    try:
                        if self.grid[nx][ny] != 0:
                            self.grid[nx][ny] += 1

                        if self.grid[nx][ny] > 9:
                            stack.append((nx, ny))
                    except IndexError:
                        pass

        return blinks

    def is_synchronized(self) -> bool:
        for line in self.grid:
            if any([x != 0 for x in line]):
                return False
        return True
