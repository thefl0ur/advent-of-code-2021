from collections import deque


def get_increments_count(file_path: str, window_size: int = 1) -> int:
    sum, current = 0, None
    file = open(file_path, 'r')
    data = deque(
        map(int, [file.__next__() for _ in range(window_size)]),
        maxlen=4,
    )
    for line in file:
        current = int(line)
        if data.popleft() < current:
            sum += 1
        data.append(current)

    file.close()
    return sum


def part1(file_path: str) -> int:
    return get_increments_count(file_path)


def part2(file_path: str) -> int:
    return get_increments_count(file_path, 3)
