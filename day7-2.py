import json

with open("inputd7.txt", "r") as f:
    data = f.readlines()

current_position: list[str] = []
folder_tree = {'/': {}}
sizes = []

def manage_command(line: str):

    command = line.split(" ")[1]
    
    if(command == "ls"):
        return

    if(command == "cd"):
        folder = line.split(" ")[2]

        if(folder == ".."):
            current_position.pop()

        else:
            current_position.append(folder)


def manage_list(line: str):
    size_or_type, name = line.split(" ")
    current_dict = folder_tree

    for pos in current_position:
        current_dict = current_dict[pos]

    if(size_or_type.isnumeric()):
        current_dict[name] = size_or_type

    else:
        current_dict[name] = {}


def calculate_sizes(tree: dict[str, str | dict]) -> int:
    total = 0
    for key, value in tree.items():

        if(isinstance(value, dict)):
            sub_size = calculate_sizes(value)
            total += sub_size
            # if(sub_size < 100_000):
            sizes.append(sub_size)
            continue
        
        if(value.isnumeric()):
            total += int(value)

    return total
            


for i, line in enumerate(data):
    
    line = line.strip()

    if(line[0] == "$"):
        manage_command(line)

    else:
        manage_list(line)


print(json.dumps(folder_tree, indent=2))

full_size = calculate_sizes(folder_tree)
unused_space = 70_000_000 - full_size
needed_space = 30_000_000
to_remove = needed_space - unused_space
smallest = max(sizes)

for size in sizes:
    print(size)
    if(size > to_remove and size < smallest):
        smallest = size

print(smallest, unused_space, needed_space, to_remove)



