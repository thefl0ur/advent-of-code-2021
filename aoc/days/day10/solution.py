RANKS = {')': 3, ']': 57, '}': 1197, '>': 25137}
FIXING_RANKS = {'(': 1, '{': 3, '[': 2, '<': 4}


def read_data(file_name: str):
    data = []
    with open(file_name, 'r') as file:
        data = [[char for char in line.strip()] for line in file]
    return data


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
    have_error = False
    for index in range(len(line)):
        if line[index] in FIXING_RANKS.keys():
            stack.append(line[index])
        else:
            bracket = stack.pop()
            if bracket == '(' and line[index] != ')':
                have_error = True
                break
            if bracket == '[' and line[index] != ']':
                have_error = True
                break
            if bracket == '{' and line[index] != '}':
                have_error = True
                break
            if bracket == '<' and line[index] != '>':
                have_error = True
                break

    if have_error:
        return None
    else:
        return stack


def falc_fixing_score(stack):
    summ = 0
    stack.reverse()
    for char in stack:
        summ = (summ * 5) + FIXING_RANKS[char]
    return summ


def part1(file_path: str) -> int:
    with open(file_path, 'r') as file:
        incorrect = [char for line in file if (char := process_line(line.strip()))]
    return sum(
        RANKS[x] for x in incorrect
    )


def part2(file_path: str) -> int:
    data = read_data(file_path)
    scores = []
    for line in data:
        fix_stack = process_inc_line(line)
        if fix_stack is not None:
            scores.append(falc_fixing_score(fix_stack))
    scores.sort()
    return scores[int((len(scores) - 1)/2)]
