from re import findall

with open("input5", "r") as f:
    all_lines = f.readlines()


def initialize_stacks():
    stacks = {i: [] for i in range(1, 10)}
    for line in all_lines[:8]:
        for idx, letter in filter(lambda pair: pair[1].isalpha(), enumerate(line)):
            stacks[(idx-1) // 4 + 1].append(letter)
    for i in stacks:
        stacks[i].reverse()
    return stacks


def parse_instruction(instruction):
    return [int(x) for x in findall("[0-9]+", instruction)]


def part1():
    stacks = initialize_stacks()
    instructions = map(parse_instruction, all_lines[10:])
    for instr in instructions:
        for _ in range(instr[0]):
            stacks[instr[2]].append(stacks[instr[1]][-1])
            del stacks[instr[1]][-1]
    return "".join([stacks[i][-1] for i in stacks])


def part2():
    stacks = initialize_stacks()
    instructions = map(parse_instruction, all_lines[10:])

    for instr in instructions:
        stacks[instr[2]] += stacks[instr[1]][-instr[0]:]
        del stacks[instr[1]][-instr[0]:]
    return "".join([stacks[i][-1] for i in stacks])


print("Part 1:", part1())
print("Part 2:", part2())
