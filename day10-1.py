with open("inputd10.txt", "r") as f:
    data = f.readlines()


register_value = 1
current_cycle = 1
checks = [20, 60, 100, 140, 180, 220]
total = 0

def has_to_verify(register_value, current_cycle):
    global checks
    if(current_cycle in checks):
        print(f"Has to check at {current_cycle}")
        return current_cycle * register_value

    return 0

for line in data:
    line = line.strip()
    print(line, current_cycle, register_value)
    command = line.split(" ")[0]


    if(command == "addx"):
        to_add = int(line.split(" ")[1])
        for i in range(2):
            total += has_to_verify(register_value, current_cycle)
            current_cycle += 1

        register_value += to_add

    elif(command == "noop"):
        total += has_to_verify(register_value, current_cycle)
        current_cycle += 1
        continue

    else:
        raise Exception("Unknown Command")


print(total)
        

