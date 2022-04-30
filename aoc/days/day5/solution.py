from typing import List

class Line:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    #todo
    #def is_horizontal
    #def is_vertical
    #def is_diag

    def get_all_points(self):
        x = list(range(min(self.x1, self.x2), max(self.x1, self.x2) + 1)) if self.x1 != self.x2 else [self.x1]
        y = list(range(min(self.y1, self.y2), max(self.y1, self.y2) + 1)) if self.y1 != self.y2 else [self.y1]
        return {'x': x, "y": y}        

def read_data(file_name: str) -> List[str]:
    data = []
    with open(file_name, 'r') as file:
        for line in file:
           vector = line.split('->')
           data.append(Line(*[int(x) for x in vector[0].split(',')], *[int(x) for x in vector[1].split(',')]))
    return data

def part1(file_path: str) -> int:
    lines = read_data(file_path)

    part1_data = []
    max_x = 0
    max_y = 0
    for line in lines:
        points = line.get_all_points()
        if len(points['x']) == 1 or len(points['y']) == 1:
            if len(points['x']) > len(points['y']):
                points['y'] = points['y']*len(points['x'])

            if len(points['y']) > len(points['x']):
                points['x'] = points['x']* len(points['y'])

            part1_data.append(points)
            if max(points['x']) > max_x:
                max_x = max(points['x'])

            if max(points['y']) > max_y:
                max_y = max(points['y'])

    vent_map = [ ['.' for x in range(max_x  + 1)] for y in  range(max_y + 1)]

    for data in part1_data:
        for index in range(len(data['x'])):
            if vent_map[data['x'][index]][data['y'][index]] == '.':
                vent_map[data['x'][index]][data['y'][index]] = 1
            else:
                vent_map[data['x'][index]][data['y'][index]] += 1

    summ = 0
    for row in vent_map:
        summ += sum(isinstance(x, int) and x > 1 for x in row)
    
    return summ

def part2(file_path: str) -> int:
    lines = read_data(file_path)

    part1_data = []
    max_x = 0
    max_y = 0
    for line in lines:
        points = line.get_all_points()
        if len(points['x']) == 1 or len(points['y']) == 1:
            if len(points['x']) > len(points['y']):
                points['y'] = points['y']*len(points['x'])

            if len(points['y']) > len(points['x']):
                points['x'] = points['x']* len(points['y'])

            part1_data.append(points)
            if max(points['x']) > max_x:
                max_x = max(points['x'])

            if max(points['y']) > max_y:
                max_y = max(points['y'])
        else:
            if all(x in points['x'] for x in  points['y']):
                part1_data.append(points)
                if max(points['x']) > max_x:
                    max_x = max(points['x'])

                if max(points['y']) > max_y:
                    max_y = max(points['y'])

    vent_map = [ ['.' for x in range(max_x  + 1)] for y in  range(max_y + 1)]

    for data in part1_data:
        for index in range(len(data['x'])):
            if vent_map[data['x'][index]][data['y'][index]] == '.':
                vent_map[data['x'][index]][data['y'][index]] = 1
            else:
                vent_map[data['x'][index]][data['y'][index]] += 1

    summ = 0
    for row in vent_map:
        summ += sum(isinstance(x, int) and x > 1 for x in row)
    
    return summ
