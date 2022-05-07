from collections import Counter
from typing import List, Dict

Graph = Dict[str, List[str]]


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


def vertex_filter_1(vertex: str, path: List[str]) -> bool:
    return vertex.isupper() or vertex not in path


def vertex_filter_2(vertex: str, path: List[str]) -> bool:
    if vertex in ['start']:
        return False

    small_cntr = Counter([cave for cave in path if cave.islower()])
    is_small = small_cntr[vertex] != 2 and small_cntr.most_common(1)[0][1] != 2

    return vertex_filter_1(vertex, path) or is_small


def find_all_path(graph: Graph, filter_func: callable) -> List[List[str]]:
    paths = ([['start']])

    valid_path = []
    while paths:
        current_path = paths.pop()
        last_vertex = current_path[-1]

        if last_vertex == 'end':
            valid_path.append(current_path)
            continue

        for connected_vertex in graph[last_vertex]:
            if filter_func(connected_vertex, current_path):
                paths.append(current_path + [connected_vertex])

    return valid_path


def part1(file_path: str) -> int:
    graph = build_graph(read_data(file_path))
    finded = find_all_path(graph, vertex_filter_1)
    return len(finded)


def part2(file_path: str) -> int:
    graph = build_graph(read_data(file_path))
    finded = find_all_path(graph, vertex_filter_2)
    return len(finded)
