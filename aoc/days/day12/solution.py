from typing import List, TypedDict

Graph = TypedDict('Graph', {'node': str, 'connected': List[str]})


def read_data(filename: str) -> List[str]:
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


def build_graph(data: List[str]) -> Graph:
    graph = {}
    for part in data:
        start, end = part.split('-')

        if start not in graph:
            graph[start] = []

        if end not in graph:
            graph[end] = []

        if end not in graph[start]:
            graph[start].append(end)

        if start not in graph[end]:
            graph[end].append(start)

    return graph


def finder(graph: Graph, path: List[str], tolerance: int) -> int:
    if path[-1] == 'end':
        return 1

    count = 0
    for connected in graph[path[-1]]:
        if connected == 'start':
            continue

        if connected.islower() and connected in path:
            if tolerance == 1:
                continue
            else:
                count += finder(graph, path + [connected], 1)
                continue

        count += finder(graph, path + [connected], tolerance)

    return count


def part1(file_path: str) -> int:
    graph = build_graph(read_data(file_path))
    return finder(graph, ['start'], 1)


def part2(file_path: str) -> int:
    graph = build_graph(read_data(file_path))
    return finder(graph, ['start'], 2)
