def part1(input_file: str) -> int:
    depth, horizontal = 0, 0
    with open(input_file, 'r') as file:
        for line in file:
            (vector, value) = line.split(' ', 2)
            value = int(value)
            if vector == 'forward':
                horizontal += value
            else:
                depth += value if vector == 'down' else - value

    return horizontal * depth


def part2(input_file: str) -> int:
    aim, depth, horizontal = 0, 0, 0
    with open(input_file, 'r') as file:
        for line in file:
            vector, value = line.split(' ', 2)
            value = int(value)
            if vector == 'forward':
                horizontal += value
                depth += aim * value
            else:
                aim += value if vector == 'down' else - value

    return horizontal * depth
