from typing import List, Set, Tuple

Point = Tuple[int, int]
Folding = Tuple[str, int]


def parce_data(file_path: str) -> Tuple[Set[Point], List[Folding]]:
    points = set()
    foldings = []
    separator_finded = False

    file = open(file_path)
    for data in file:
        data = data.strip()

        if data == '':
            separator_finded = True
            continue

        if not separator_finded:
            points.add(tuple(map(int, data.split(','))))
        else:
            foldings.append((data[11], int(data[13:])))
    file.close()

    return points, foldings


def print_code(points: Set[Point]) -> None:
    max_x = max([x[0] for x in points])
    max_y = max([x[1] for x in points])
    matrix = [[0 for x in range(max_x+1)] for y in range(max_y+1)]

    for point in points:
        x, y = point
        matrix[y][x] = '#'

    for y in range(max_y+1):
        string = ""
        for x in range(max_x+1):
            if matrix[y][x] != '#':
                string += ' .'
            else:
                string += ' #'
        print(string)


def fold(points: List[Point], fold_instruction: Folding) -> Set[Point]:
    orientation, position = fold_instruction

    new_points = set()
    while points:
        point = points.pop()

        if orientation == 'y':
            if point[1] > position:
                new_points.add((point[0], 2*position - point[1]))
            else:
                new_points.add(point)
        else:
            if point[0] > position:
                new_points.add((2*position - point[0], point[1]))
            else:
                new_points.add(point)

    return new_points


def part1(file_path: str) -> int:
    points, foldings = parce_data(file_path)
    tmp = fold(points, foldings[0])

    return len(tmp)


def part2(file_path: str) -> int:
    points, foldings = parce_data(file_path)

    while foldings:
        points = fold(points, foldings.pop(0))

    print_code(points)
    return 0
