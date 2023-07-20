with open("input5", "r") as f:
    all_lines = f.readlines()

starting_state = all_lines[:8]
stacks = ['']*9
instructions = all_lines[10:]
# initialize lists:
for row in range(8):
    for col in range(1, len(starting_state[row]), 4):
        if starting_state[row][col] != ' ':
            stacks[(col-1)//4] += starting_state[row][col]

for instr in instructions:
    instr = instr.split()
    amt = int(instr[1])
    start = int(instr[3]) - 1
    end = int(instr[5]) - 1

    for _ in range(amt):
        stacks[end] = stacks[start][0] + stacks[end]
        stacks[start] = stacks[start][1:]

print([stacks[i][0] for i in range(9)])
