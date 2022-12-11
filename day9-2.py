with open("inputd9.txt", "r") as f:
    data = f.readlines()

class Axis():
    X, Y = range(0, 2)

pos_map: list[list[str]] = []
row_column = 1000

for _ in range(row_column):
    temp_arr = []
    for _ in range(row_column):
        temp_arr.append(".")

    pos_map.append(temp_arr)

# print(pos_map)


def is_touching(head_pos: list[int], tail_pos: list[int]) -> bool:
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if(tail_pos[Axis.X] + j == head_pos[Axis.X] and tail_pos[Axis.Y] + i == head_pos[Axis.Y]):
                return True

    return False

def run_action(direction: str, head_pos: list[int], tail_pos: list[int], is_head: bool = False) -> tuple[list[int], list[int]]:

    if(is_head):
        if(direction == "U"):
            head_pos[Axis.Y] -= 1

        elif(direction == "D"):
            head_pos[Axis.Y] += 1

        elif(direction == "L"):
            head_pos[Axis.X] -= 1

        elif(direction == "R"):
            head_pos[Axis.X] += 1

        else:
            raise Exception("Unknown direction")

    if(is_touching(head_pos, tail_pos)):
        return head_pos, tail_pos

    # Check 2 to the right
    if(tail_pos[Axis.X] + 2 == head_pos[Axis.X] and tail_pos[Axis.Y] == head_pos[Axis.Y]):
        tail_pos = [tail_pos[Axis.X] + 1, tail_pos[Axis.Y]]
        return head_pos, tail_pos

    # Check 2 to the left
    if(tail_pos[Axis.X] - 2 == head_pos[Axis.X] and tail_pos[Axis.Y] == head_pos[Axis.Y]):
        tail_pos = [tail_pos[Axis.X] - 1, tail_pos[Axis.Y]]
        return head_pos, tail_pos

    # Check 2 up
    if(tail_pos[Axis.X] == head_pos[Axis.X] and tail_pos[Axis.Y] + 2 == head_pos[Axis.Y]):
        tail_pos = [tail_pos[Axis.X], tail_pos[Axis.Y] + 1]
        return head_pos, tail_pos

    # Check 2 down
    if(tail_pos[Axis.X] == head_pos[Axis.X] and tail_pos[Axis.Y] - 2 == head_pos[Axis.Y]):
        tail_pos = [tail_pos[Axis.X], tail_pos[Axis.Y] - 1]
        return head_pos, tail_pos


    for i in [-1, 1]:
        for j in [-1, 1]:
            temp_pos = [tail_pos[Axis.X] + i, tail_pos[Axis.Y] + j]
            if(is_touching(temp_pos, head_pos)):
                tail_pos = temp_pos
                return head_pos, tail_pos

    raise Exception("Error")

rope_length = 10
rope = []
for _ in range(rope_length):
    rope.append([500, 500])

pos_map[rope[0][Axis.X]][rope[0][Axis.Y]] = "*"
print(rope)

for line in data:
    line = line.strip()
    direction, amount = line.split(" ")
    # print(head_pos, tail_pos, direction, amount)
    for _ in range(int(amount)):
        for i, _ in enumerate(rope[:-1]):
            if(i == 0):
                rope[i], rope[i + 1] = run_action(direction, rope[i], rope[i + 1], is_head=True)
            else:
                rope[i], rope[i + 1] = run_action(direction, rope[i], rope[i + 1])
                
        pos_map[rope[-1][Axis.X]][rope[-1][Axis.Y]] = "*"
            

count = 0
for row in pos_map:
    for elem in row:
        if(elem == "*"):
            count += 1


print(count)
