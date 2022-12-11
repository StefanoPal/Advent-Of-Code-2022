import copy
with open("inputd8.txt", "r") as f:
    data = f.readlines()


def check_up(to_check, i, j, tree):
    global total
    visible = True

    for k in range(0, i):
        if(to_check[k][j] >= tree): 
            visible = False
            break

    # print(f"UP: checked {tree} against {[row[j] for row in to_check[0:i]]}")
    
    if(visible):
        total += 1
        
    return visible

def check_down(to_check, i, j, tree):
    global total
    visible = True

    for k in range(i + 1, len(to_check)):
        if(to_check[k][j] >= tree): 
            visible = False
            break

    # print(f"DOWN: checked {tree} against {[row[j] for row in to_check[i+1:len(to_check)]]}")

    if(visible):
        total += 1
        
    return visible

def check_left(to_check, i, j, tree):
    global total
    visible = True

    for k in range(0, j):
        if(to_check[i][k] >= tree): 
            visible = False
            break
    
    # print(f"LEFT: checked {tree} against {to_check[i][0:j]}")

    if(visible):
        total += 1
        
    return visible

def check_right(to_check, i, j, tree):
    global total
    visible = True

    for k in range(j + 1, len(to_check[0])):
        if(to_check[i][k] >= tree): 
            visible = False
            break
    
    # print(f"RIGHT: checked {tree} against {to_check[i][j+1:len(to_check[0])]}")

    if(visible):
        total += 1
        
    return visible


matrix_map: list[list] = []

for line in data:
    line = line.strip()
    matrix_map.append(list([int(i) for i in line]))

to_check = copy.deepcopy(matrix_map)

total = (len(matrix_map[0]) * 4) - 4

for i, _ in enumerate(to_check):
    to_check[i].pop()
    to_check[i].pop(0)

to_check.pop()
to_check.pop(0)

for i, row in enumerate(to_check):
    for j, tree in enumerate(row):
        tree = int(tree)
        # print(f"tree {tree}, row {i + 1}, column {j + 1}")

        if(check_up(matrix_map, i + 1, j + 1, tree)): 
            continue

        if(check_down(matrix_map, i + 1, j + 1, tree)):
            continue

        if(check_left(matrix_map, i + 1, j + 1, tree)): 
            continue

        if(check_right(matrix_map, i + 1, j + 1, tree)): 
            continue

    # break

print(total)