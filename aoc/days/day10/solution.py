RANKS = {')': 3, ']': 57, '}': 1197, '>': 25137}
FIXING_RANKS = {'(': 1, '{': 3, '[': 2, '<': 4}


def process_line(line):
    stack = []
    for char in line:
        if char in FIXING_RANKS.keys():
            stack.append(char)
        else:
            if abs(ord(stack.pop()) - ord(char)) > 2:
                return char


def process_inc_line(line):
    stack = []
    for char in line:
        if char in FIXING_RANKS.keys():
            stack.append(char)
        elif abs(ord(stack.pop()) - ord(char)) > 2:
            return None
    return stack


def calc_fixing_score(stack):
    summ = 0
    for char in reversed(stack):
        summ = summ * 5 + FIXING_RANKS[char]
    return summ


def part1(file_path: str) -> int:
    with open(file_path, 'r') as file:
        incorrect = [char for line in file if (char := process_line(line.strip()))]
    return sum(
        RANKS[x] for x in incorrect
    )


def part2(file_path: str) -> int:
    with open(file_path, 'r') as file:
        scores = sorted(
            [
                calc_fixing_score(fix_stack) for line in file
                if (fix_stack := process_inc_line(line.strip()))
            ]
        )
    return scores[int((len(scores) - 1)/2)]
