from enum import Enum
with open("inputd2.txt", "r") as f:
    data = f.readlines()


class roundType(Enum):
    Rock = 0
    Paper = 1
    Scissors = 2

playerDict = {'A': roundType.Rock, 'B': roundType.Paper, 'C': roundType.Scissors}
winningDict = {roundType.Rock: roundType.Paper, roundType.Scissors: roundType.Rock, roundType.Paper: roundType.Scissors}
losingDict = {roundType.Rock: roundType.Scissors, roundType.Scissors: roundType.Paper, roundType.Paper: roundType.Rock}
points = {roundType.Rock: 1, roundType.Paper: 2, roundType.Scissors: 3}
# A = Rock, B = Paper, C = Scissors
# X = Lose, Y = Draw, Z = Win
# Rock > Scissors > Paper > Rock

def get_right_move(player: roundType, rule: str):

    if(rule == 'X'):
        return 0, losingDict[player]

    elif(rule == 'Y'):
        return 3, player

    else:
        return 6, winningDict[player]

total = 0
for line in data:
    line = line.strip()
    player = line.split(" ")[0]
    rule = line.split(" ")[1]
    
    score, move = get_right_move(playerDict[player], rule)

    total += (score + points[move])

print(total)