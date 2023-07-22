class Register:
    def __init__(self):
        self.value = 1
        self.cycles = 0
        self.part1_answer = 0
        self.part2_string = ''

    def addx(self, x):
        self.noop()
        self.noop()
        self.value += x

    def noop(self):
        self.cycles += 1
        if self.cycles in [20, 60, 100, 140, 180, 220]:
            self.part1_answer += self.strength()
        self.draw_pixel()

    def strength(self):
        return self.cycles * self.value

    def draw_pixel(self):
        if abs(self.value - (self.cycles-1) % 40) <= 1:
            self.part2_string += "#"
        else:
            self.part2_string += "."


with open("input10", "r") as f:
    lines = map(str.split, f.readlines())

r = Register()
for line in lines:
    if line[0] == "noop":
        r.noop()
    else:
        r.addx(int(line[1]))

print("Part 1:", r.part1_answer)
print("Part 2:\n", "".join([r.part2_string[40*i:40*(i+1)]+"\n" for i in range(6)]))
