from typing import List, Tuple, TypedDict, Union

Matrix = List[List[Union[str, int]]]
Points = TypedDict('Points', {'x': List[int], 'y': List[int]})


class Line:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def get_all_points(self) -> Points:
        x = self._get_line(self.x1, self.x2)
        y = self._get_line(self.y1, self.y2)

        return {'x': x, "y": y}

    def _get_line(self, start: int, end: int) -> List[int]:
        if start == end:
            return [start]

        direction = 1 if start < end else -1
        return list(range(start, end + direction, direction))


def read_data(file_name: str) -> List[Line]:
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            vector = line.split('->')
            data.append(
                Line(
                    *[int(x) for x in vector[0].split(',')],
                    *[int(x) for x in vector[1].split(',')],
                ),
            )
    return data


def get_lines_points(
    lines: List[Line], use_diagonal: bool = False
) -> Tuple[List[Points], int, int]:
    points = []
    max_x = 0
    max_y = 0
    for line in lines:
        line_points = line.get_all_points()
        if len(line_points['x']) == 1 or len(line_points['y']) == 1:
            if len(line_points['x']) > len(line_points['y']):
                line_points['y'] = line_points['y'] * len(line_points['x'])

            if len(line_points['y']) > len(line_points['x']):
                line_points['x'] = line_points['x'] * len(line_points['y'])

            points.append(line_points)
            max_x = max(max(line_points['x']), max_x)
            max_y = max(max(line_points['y']), max_y)

        elif use_diagonal:
            points.append(line_points)
            max_x = max(max(line_points['x']), max_x)
            max_y = max(max(line_points['y']), max_y)

    return (points, max_x, max_y)


def build_map(points: List[Points], max_x: int, max_y: int) -> Matrix:
    vents_map = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for data in points:
        for index, _ in enumerate(data['y']):
            vents_map[data['y'][index]][data['x'][index]] += 1

    return vents_map


def get_intersections(vents_map: Matrix) -> int:
    def filter_expression(value):
        return value > 1

    return sum(len(list(filter(filter_expression, row))) for row in vents_map)


def part1(file_path: str) -> int:
    lines = read_data(file_path)

    line_points, max_x, max_y = get_lines_points(lines)

    vent_map = build_map(line_points, max_x, max_y)

    return get_intersections(vent_map)


def part2(file_path: str) -> int:
    lines = read_data(file_path)

    line_points, max_x, max_y = get_lines_points(lines, True)

    vent_map = build_map(line_points, max_x, max_y)

    return get_intersections(vent_map)
