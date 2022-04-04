def read_data(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def build_graph(data):
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

def vertex_filter_1(vertex, path):
    return vertex.isupper() or vertex not in path

from collections import Counter

def vertex_filter_2(vertex, path):
    if vertex in ['start']:
        return False
    
    small_cntr = Counter([cave for cave in path if cave.islower()])
    is_small = small_cntr[vertex] != 2 and small_cntr.most_common(1)[0][1] != 2

    return vertex_filter_1(vertex, path) or is_small

def find_all_path(graph, filter_func):
    paths= ([['start']])

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

        # breakpoint()
    return valid_path

graph = build_graph(read_data('data/input.in'))

# print(graph)

# num_path = 0
# finded = find_all_path(graph, vertex_filter_1)
finded = find_all_path(graph, vertex_filter_2)

# for find in finded:
#     print(",".join(find))

print(len(finded))