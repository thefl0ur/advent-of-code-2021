from typing import List

class Dive:
    horizontal = 0
    depth = 0

    def __init__(self, data: List[str]):
        self.data = data

    def calculcate_position(self) -> int:
        for line in self.data:
            vector, value = self._parce_line(line)

            if vector == 'up':
                self.depth -= int(value)
            
            if vector == 'down':
                self.depth += int(value);

            if vector == 'forward':
                self.horizontal += int(value)

        return self.horizontal * self.depth;

    def _parce_line(self, line: str):
        vector, value = line.split(' ')
        return vector, value


class DiveAim(Dive):
    aim = 0

    def calculcate_position(self) -> int:
        for line in self.data:
            vector, value = self._parce_line(line)

            if vector == 'up':
                self.aim -= int(value)
            
            if vector == 'down':
                self.aim += int(value)

            if vector == 'forward':
                self.horizontal += int(value)
                self.depth += self.aim * int(value)

        return self.horizontal * self.depth;
