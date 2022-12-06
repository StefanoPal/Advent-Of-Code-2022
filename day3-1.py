from typing import Union

with open("inputd3.txt", "r") as f:
    data = f.readlines()


def get_priority(char: str) -> int:

    if char.islower():
        return ord(char) - 96

    else:
        return ord(char) - 38

total = 0
for line in data:
    line = line.strip()
    first_half, second_half = list(line[: int(len(line) / 2)]), list(line[int(len(line) / 2) :])
    common = set(first_half).intersection(set(second_half))
    total += get_priority(''.join(common))

print(total)
