from typing import List, Tuple


class NoDataException(Exception):
    ...


class SonarSweep:
    current_index = 0
    current_value = None

    def __init__(
        self,
        data: List[int],
        window_size: int = 1
    ) -> None:
        self.window_size = window_size
        self.data = data

    def _get_next_window_pair(self) -> Tuple[List[int], List[int]]:
        if len(self.data) < self.current_index + 1 + self.window_size:
            raise NoDataException

        value1 = self.data[self.current_index: self.current_index + self.window_size]
        self.current_index += 1

        value2 = self.data[self.current_index: self.current_index + self.window_size]
      
        return value1, value2

    def get_increments_count(self) -> int:
        increments_count = 0
        while True:
            try:
                value1, value2 = self._get_next_window_pair()
            except NoDataException:
                break
            
            if (sum(value1) < sum(value2)):
                increments_count += 1
                
        return increments_count
