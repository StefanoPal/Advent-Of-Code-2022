from enum import Enum
with open("input.txt", "r") as f:
    data = f.readlines()


class roundType(Enum):
    Rock = 0
    Paper = 1
    Scissors = 2

versusDict = {'A': roundType.Rock, 'B': roundType.Paper, 'C': roundType.Scissors}
playerDict = {'X': roundType.Rock, 'Y': roundType.Paper, 'Z': roundType.Scissors}

# A = Rock, B = Paper, C = Scissors
# X = Rock, Y = Paper, Z = Scissors
# Rock > Scissors > Paper > Rock

def check_win(player: roundType, versus: roundType) -> bool:

    if(player == roundType.Rock and versus == roundType.Scissors):
        return True

    if(player == roundType.Scissors and versus == roundType.Paper):
        return True

    if(player == roundType.Paper and versus == roundType.Rock):
        return True

    return False

points = {'X': 1, 'Y': 2, 'Z': 3}
total = 0
for line in data:
    line = line.strip()
    first_char = line.split(" ")[0]
    second_char = line.split(" ")[1]
    print(first_char, second_char)

    if(versusDict[first_char] == playerDict[second_char]):
        total += (3 + points[second_char])
        continue

    if(check_win(playerDict[second_char], versusDict[first_char])):
        total += (6 + points[second_char])
    
    else:
        total += points[second_char]

print(total)