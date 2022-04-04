from typing import List
import statistics

def read_data(file_name: str) -> List[str]:
    data = []
    with open(file_name, 'r') as file:
        # breakpoint()
        data = [int(x) for x in file.readline().split(',')]
    return data

data = read_data('data/input.in')
target_point = statistics.median(data)
print(sum([abs(x - target_point) for x in data]))