class BT:  # Block and tower
    def __init__(self, demo=False):
        self.tower = {i: [i == 0]*7 for i in range(5)}
        self.tower_height = 0
        self.block_counter = 0
        self.block = [[x, 4] for x in range(2, 6)]
        self.jet_counter = -1
        fname = "practice17" if demo else "input17"
        with open(fname, "r") as f:
            self.jets = [s for s in f.read().rstrip("\n")]
        self.jet_length = len(self.jets)
        self.memos = {}

        self.basic_shapes = [
            [[x, 0] for x in range(2, 6)],  # ---- shape
            [[x, 1] for x in range(2, 5)] + [[3, 0], [3, 2]],  # + shape
            [[x, 0] for x in range(2, 5)] + [[4, 1], [4, 2]],  # _| shape
            [[2, y] for y in range(4)],  # | shape
            [[2 + x, y] for x in range(2) for y in range(2)]  # square
        ]

    def get_new_block(self):
        self.block_counter = (self.block_counter + 1) % 5
        self.block = [[c[0], c[1] + self.tower_height+4] for c in self.basic_shapes[self.block_counter]]
        return

    def update_tower_height(self):
        tmp = max(map(lambda c: c[1], self.block))
        if self.tower_height < tmp:
            self.tower_height = tmp
            for i in range(max(self.tower) + 1, self.tower_height + 8):
                self.tower[i] = [False]*7
        return

    def drop_block(self):
        for c in self.block:
            c[1] -= 1
        return

    def move_block(self):
        # Get direction
        self.jet_counter = (self.jet_counter + 1) % self.jet_length
        d = ord(self.jets[self.jet_counter]) - 61  # Will be +/- 1
        # First, check if it can be moved:
        if any(c[0] == 3 + 3*d for c in self.block):  # If block is touching side wall
            return
        if any(self.tower[c[1]][c[0] + d] for c in self.block):  # If block is touching a stopped block
            return
        for c in self.block:
            c[0] += d
        return

    def is_stopped(self):
        return any(self.tower[c[1]-1][c[0]] for c in self.block)

    def freeze_current_block(self):
        for c in self.block:
            self.tower[c[1]][c[0]] = True
        return

    def simulate_blocks(self, nblocks):
        b = 1  # Counts the block that we are currently dropping
        while b <= nblocks:
            while True:
                self.move_block()
                if self.is_stopped():
                    break
                self.drop_block()
            # Block is stopped
            self.freeze_current_block()
            self.simplify_grid()
            self.update_tower_height()

            # Store state
            if self.tower_mask() in self.memos:
                mem = self.memos[self.tower_mask()]
                b_0 = mem[0]
                h_0 = mem[1]
                delta_b = b - b_0
                delta_h = self.tower_height - h_0
                n_cycles = (nblocks - b)//delta_b

                b = b + n_cycles * delta_b
                self.tower_height = self.tower_height + n_cycles * delta_h
                self.tower = {t + n_cycles * delta_h: self.tower[t] for t in self.tower}
                self.memos = {}  # A bit wasteful since we'll refill this dict, but it's not too bad.
            else:
                self.memos[self.tower_mask()] = (b, self.tower_height)
            b += 1
            # Now prepare a new block for next time
            self.get_new_block()
        return self.tower_height

    def simplify_grid(self):
        for y in set([c[1] + 1 for c in self.block] + [c[1] - 1 for c in self.block]):
            if all(map(lambda x: x[0] or x[1], zip(self.tower[y], self.tower[y+1]))):
                for height in list(self.tower):
                    if height < y:
                        del self.tower[height]
                return
        return

    def tower_mask(self):
        return ''.join([str(int(b)) for row in range(min(self.tower), max(self.tower) + 1) for b in self.tower[row]]).join([str(self.block_counter), str(self.jet_counter)])


print("Part 1:", BT(demo=False).simulate_blocks(2022))
print("Part 2:", BT(demo=False).simulate_blocks(1000000000000))
