from typing import Union

with open("inputd3.txt", "r") as f:
    data = f.readlines()


def get_priority(char: str) -> int:

    if char.islower():
        return ord(char) - 96

    else:
        return ord(char) - 38

def get_line(initial: int, offset: int = 0) -> list[str]:
    return list(data[initial + offset].strip())

total = 0

for i in range(0, len(data), 3):
    first_line = set(get_line(i))
    # print(first_line)

    for j in range(1, 3):
        first_line = first_line.intersection(set(get_line(i, j)))

    total += get_priority(''.join(first_line))

print(total)
