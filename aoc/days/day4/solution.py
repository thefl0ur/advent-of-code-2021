from typing import List, Tuple

MARKED = 'X'
Matrix = List[List[int]]


class Board:
    def __init__(self, matrix: Matrix) -> None:
        self.matrix = matrix

    def mark_number(self, number: int) -> None:
        for column, _ in enumerate(self.matrix[0]):
            for row, _ in enumerate(self.matrix):
                if self.matrix[column][row] == number:
                    self.matrix[column][row] = MARKED

    def is_winning(self) -> bool:
        for line in self.matrix:
            if all(x == MARKED for x in line):
                return True

        for index, _ in enumerate(self.matrix):
            if all(x == MARKED for x in [row[index] for row in self.matrix]):
                return True

    def summ(self) -> int:
        return sum([item for sublist in self.matrix for item in sublist if item != MARKED])


def parce_input(file_path: str) -> Tuple[List[int], List[Matrix]]:
    file = open(file_path, 'r')
    game_input = list(map(int, file.__next__().split(',')))

    fields = []
    for line in file:
        if (line.rstrip() != ''):
            fields[-1].append(list(map(int, line.split())))
        else:
            fields.append([])

    file.close()
    return (game_input, fields)


def part1(file_path: str) -> int:
    game_input, fields = parce_input(file_path)
    boards = [Board(field) for field in fields]
    for number in game_input:
        for board in boards:
            board.mark_number(number)
            if board.is_winning():
                return board.summ() * number


def part2(file_path: str) -> int:
    game_input, fields = parce_input(file_path)
    boards = [Board(field) for field in fields]

    for number in game_input:
        winners_indexes = []
        for index, board in enumerate(boards):
            board.mark_number(number)
            if board.is_winning():
                winners_indexes.append(index)

        if (len(boards)) == 1:
            return boards[0].summ() * number
        else:
            for index in reversed(winners_indexes):
                del boards[index]
