import operator
from typing import Callable
from math import floor
from typing import TypedDict
with open("inputd11.txt", "r") as f:
    data = f.read()


class TestDict(TypedDict):
    value: Callable[[int], bool]
    true: int
    false: int

class MonkeyDict(TypedDict):
    items: list[int]
    operation: Callable[[int], int]
    test: TestDict
    inspected: int


ops = { "+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv }

def build_elem(monkey: str) -> MonkeyDict:
    global ops
    item_line = monkey.split("\n")[1]
    op_line = monkey.split("\n")[2]
    test_line = monkey.split("\n")[3]
    if_true_line = monkey.split("\n")[4]
    if_false_line = monkey.split("\n")[5]

    temp_value = op_line.split("=")[-1].strip()
    test_value = get_value(test_line)
    if_true_value = get_value(if_true_line)
    if_false_value = get_value(if_false_line)
    items_value: list[int] = []

    for elem in item_line.split(":")[-1].strip().split(","):
        items_value.append(int(elem))

    _, operation, calc_value = temp_value.split(" ")
    print(operation, calc_value)

    if(calc_value == "old"):
        op_value: Callable[[int], int] = lambda old: ops[operation](old, old)
    else:
        op_value: Callable[[int], int] = lambda old: ops[operation](int(calc_value), old)
        
    val: MonkeyDict = {
        "items": items_value,
        "operation": op_value,
        "test": {
            "value": lambda to_verify: to_verify % test_value == 0,
            "true": if_true_value,
            "false": if_false_value,
        },
        "inspected": 0
    }

    return val

def get_value(line):
    return int(line.split(" ")[-1])




monkeys: list[MonkeyDict] = []
for monkey in data.split("\n\n"):
    monkeys.append(build_elem(monkey))


for _ in range(20):
    for monkey in monkeys:

        if(len(monkey["items"]) == 0):
            continue

        while(len(monkey["items"]) != 0):
            monkey["items"][0] = monkey["operation"](monkey["items"][0])
            monkey["items"][0] = floor(monkey["items"][0] / 3)
            monkey["inspected"] += 1

            if(monkey["test"]["value"](monkey["items"][0])):
                monkeys[monkey["test"]["true"]]["items"].append(monkey["items"][0])
            else:
                monkeys[monkey["test"]["false"]]["items"].append(monkey["items"][0])

            del monkey["items"][0]


print(sorted([monkey["inspected"] for monkey in monkeys]))