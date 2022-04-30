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
        x_direction = 1
        if self.x1 > self.x2:
            x_direction = -1
        y_direction = 1
        if self.y1 > self.y2:
            y_direction = -1
        x = (
            list(range(self.x1, self.x2 + x_direction, x_direction))
            if self.x1 != self.x2
            else [self.x1]
        )
        y = (
            list(range(self.y1, self.y2 + y_direction, y_direction))
            if self.y1 != self.y2
            else [self.y1]
        )

        return {'x': y, "y": x}


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
            if max(line_points['x']) > max_x:
                max_x = max(line_points['x'])

            if max(line_points['y']) > max_y:
                max_y = max(line_points['y'])
        elif use_diagonal:
            points.append(line_points)
            if max(line_points['x']) > max_x:
                max_x = max(line_points['x'])

            if max(line_points['y']) > max_y:
                max_y = max(line_points['y'])

    return (points, max_x, max_y)


def build_map(points: List[Points], max_x: int, max_y: int) -> Matrix:
    vents_map = [['.' for x in range(max_x + 1)] for y in range(max_y + 1)]

    for data in points:
        for index in range(len(data['x'])):
            if vents_map[data['x'][index]][data['y'][index]] == '.':
                vents_map[data['x'][index]][data['y'][index]] = 1
            else:
                vents_map[data['x'][index]][data['y'][index]] += 1

    return vents_map


def get_intersections(vents_map: Matrix) -> int:
    summ = 0
    for row in vents_map:
        summ += sum(isinstance(x, int) and x > 1 for x in row)

    return summ


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
