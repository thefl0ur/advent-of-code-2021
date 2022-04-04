from typing import List

def read_data(file_name: str) -> List[int]:
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            data.append(int(line))
    return data
