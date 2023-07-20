def outcome(player1, player2):
    # player1, player2 are in {0,1,2} = {rock, paper, scissors}
    diffs = [3, 6, 0]
    return diffs[(player2-player1) % 3]


def score(player1, player2):
    return outcome(player1, player2) + (player2 + 1)


with open("input2", "r") as f:
    print(sum(map(lambda line: score(ord(line[0]) - ord("A"), ord(line[2]) - ord("X")), f.readlines())))

