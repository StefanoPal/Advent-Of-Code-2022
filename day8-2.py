import copy
with open("inputd8.txt", "r") as f:
    data = f.readlines()


def check_up(to_check, i, j, tree):
    value = 1

    for k in range(i - 1, -1, -1):
        if(to_check[k][j] < tree): 
            value += 1
        else:
            return value

    # print(f"UP: checked {tree} against {[row[j] for row in to_check[0:i]]}")
    return value - 1

def check_down(to_check, i, j, tree):
    value = 1

    for k in range(i + 1, len(to_check)):
        if(to_check[k][j] < tree): 
            value += 1
        else:
            return value

    # print(f"DOWN: checked {tree} against {[row[j] for row in to_check[i+1:len(to_check)]]}")
    return value - 1

def check_left(to_check, i, j, tree):
    value = 1

    for k in range(j - 1, -1, -1):
        if(to_check[i][k] < tree): 
            value += 1
        else:
            return value
    
    # print(f"LEFT: checked {tree} against {to_check[i][0:j]}")
    return value - 1

def check_right(to_check, i, j, tree):
    value = 1

    for k in range(j + 1, len(to_check[0])):
        if(to_check[i][k] < tree): 
            value += 1
        else:
            return value
    
    # print(f"RIGHT: checked {tree} against {to_check[i][j+1:len(to_check[0])]}")
    return value - 1


matrix_map: list[list] = []

for line in data:
    line = line.strip()
    matrix_map.append(list([int(i) for i in line]))

to_check = copy.deepcopy(matrix_map)

max_value = 0

for i, _ in enumerate(to_check):
    to_check[i].pop()
    to_check[i].pop(0)

to_check.pop()
to_check.pop(0)

for i, row in enumerate(to_check):
    for j, tree in enumerate(row):
        tree = int(tree)
        value = check_up(matrix_map, i + 1, j + 1, tree)
        value2 = check_down(matrix_map, i + 1, j + 1, tree)
        value3 = check_left(matrix_map, i + 1, j + 1, tree)
        value4 = check_right(matrix_map, i + 1, j + 1, tree)
        # print(f"tree {tree}, row {i + 1}, column {j + 1}", value, value2, value3, value4, value * value2 * value3 * value4)

        value = value * value2 * value3 * value4

        if(value > max_value): max_value = value

    # break

print(max_value)