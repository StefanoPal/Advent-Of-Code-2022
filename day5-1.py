from queue import LifoQueue
import re

with open("inputd5.txt", "r") as f:
    data = f.read()


stacks: list[LifoQueue] = []


def create_initial_stacks(data: str, stacks: list[LifoQueue]):
    rows = []
    initial = data.split("\n\n")[0]
    for row in initial.split("\n"):
        rows.append([row[i:i+4].strip() for i in range(0, len(row), 4)])

    for row in rows[:-1]:
        for i, elem in enumerate(row):

            try:
                stacks[i]
            except IndexError:
                stacks.append(LifoQueue())
        
            if(elem == ''):
                continue

            elem = re.sub(r"[\[\]]", '', elem)
            #print(elem)
            stacks[i].put(elem)

create_initial_stacks(data, stacks)

with open("inputd5.txt", "r") as f:
    instructions = f.readlines()[10:]

instructions = [i.strip() for i in instructions]
instructions = [[int(i.split(" ")[1]), int(i.split(" ")[3]), int(i.split(" ")[5])] for i in instructions]

for i, _ in enumerate(stacks):
    stacks[i].queue.reverse()

for instruction in instructions:
    #print(instruction)
    #print("\n\n\n\n")
    if(stacks[instruction[1] - 1].empty()):
        continue

    for i in range(instruction[0]):
        temp = stacks[instruction[1] - 1].get(timeout=2)
        stacks[instruction[2] - 1].put(temp)


[print(stack.queue) for stack in stacks]

