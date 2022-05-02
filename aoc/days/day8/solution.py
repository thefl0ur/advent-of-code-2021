from typing import List


def generate_list(input: str) -> List[str]:
    return [x for x in input.strip().split(' ')]


def part1(file_path: str) -> int:
    summ = 0
    file = open(file_path)
    for line in file:
        summ += sum(
            [
                1 if len(x) in [3, 4, 2, 7] else 0
                for x in generate_list(line.split('|')[1])
            ]
        )
    file.close()
    return summ


def part2(file_path: str) -> int:
    summ = 0
    file = open(file_path)
    for line in file:
        decoder = Decoder(*map(generate_list, line.split('|')))
        summ += decoder.get_decoded()
    file.close()
    return summ


class Decoder:
    def _len_to_number(self, len):
        if len == 5:
            return [2, 3, 5]
        elif len == 6:
            return [0, 6, 9]
        elif len == 2:
            return [1]
        elif len == 4:
            return [4]
        elif len == 3:
            return [7]
        return [8]

    def __init__(self, alpabet, target_number):
        self.target = target_number
        self.numbers = {num: [] for num in range(0, 10)}

        for num in alpabet:
            for candidate in self._len_to_number(len(num)):
                self.numbers[candidate].append(num)

        self._decode()

    def _decode(self):
        display = {segment: None for segment in 'abcdf'}
        set_number_1 = set(*self.numbers[1])
        set_number_4 = set(*self.numbers[4])
        display['a'] = list(set(*self.numbers[7]).difference(set_number_1))
        display['b'] = list(set(set_number_4).difference(set_number_1))
        display['c'] = list(set_number_1)
        display['d'] = list(set(set_number_4).difference(set_number_1))
        display['f'] = list(set_number_1)

        self.numbers[5] = list(
            filter(lambda x: set(display['b']).issubset(set(x)), self.numbers[5])
        )

        c_f_values = display['c']
        # self.numbers[5] contains all 5-segments number in that moment
        if c_f_values[0] in self.numbers[5][0]:
            display['f'] = c_f_values[0]
            display['c'] = c_f_values[1]
        else:
            display['f'] = c_f_values[1]
            display['c'] = c_f_values[0]

        self.numbers[2] = list(
            filter(
                lambda x: display['c'] in x and display['f'] not in x,
                list(set(self.numbers[2]) - set(self.numbers[5]))
                )
            )

        self.numbers[3] = list(
            set(self.numbers[3]) - set(self.numbers[2]) - set(self.numbers[5])
        )

        self.numbers[6] = list(
            filter(
                lambda x: display['c'] not in x,
                list(set(self.numbers[6]) - set(self.numbers[8])),
                )
            )

        display['d'] = list(set(*self.numbers[2]).intersection(set(display['d'])))
        display['b'] = list(set(display['d']).difference(set(display['d'])))

        self.numbers[9] = list(
            filter(
                lambda x: display['d'][0] in x,
                list(set(self.numbers[9]) - set(self.numbers[6])),
            )
        )

        self.numbers[0] = list(
            set(self.numbers[0]) - set(self.numbers[6]) - set(self.numbers[9])
        )

    def get_decoded(self):
        tmp = []
        for t in self.target:
            tmp += [
                str(key) for key, value in self.numbers.items() if set(t) == set(*value)
            ]
        return int("".join(tmp))
