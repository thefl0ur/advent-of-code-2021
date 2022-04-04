from typing import List

def read_data(file_name: str) -> List[str]:
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            data.append(line.rstrip())
    return data
