class Register:
    def __init__(self):
        self.value = 1
        self.cycles = 0
        self.important_cycles = [20, 60, 100, 140, 180, 220]
        self.part1_answer = 0
        self.part2_string = ''

    def addx(self, x):
        self.noop()
        self.noop()
        self.value += x

    def noop(self):
        self.cycles += 1
        if self.cycles in self.important_cycles:
            self.part1_answer += self.strength()
        self.draw_pixel()

    def strength(self):
        return self.cycles * self.value

    def draw_pixel(self):
        if abs(self.value - (self.cycles-1)%40) <= 1:
            self.part2_string += "#"
        else:
            self.part2_string += "."


def get_the_answer():
    with open("input10", "r") as f:
        r = Register()
        for line in f:
            if line[0:4] == "noop":
                r.noop()
            else:
                r.addx(int(line.split()[1]))
    return r.part1_answer, r.part2_string


a1, a2 = get_the_answer()
print(a1)
for i in range(6):
    print(a2[40*i:40*(i+1)])
