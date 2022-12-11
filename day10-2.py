from time import sleep
import sys

with open("inputd10.txt", "r") as f:
    data = f.readlines()


register_value = 1
current_cycle = 1
screen = list("."*280)

def draw(current_cycle: int, register_value: int):
    global screen
    if((current_cycle % 40) in [register_value - 1, register_value, register_value + 1]):
        screen[current_cycle] = "#"

    single_char = "\033[A"
    print(f"{single_char*8}\f")
    print_screen(screen)
    sleep(0.01)

def print_screen(screen):
    templine = ""
    for i, elem in enumerate(screen):
        if(i % 40 == 0):
            print(templine)
            templine = ""
    
        templine += elem


print_screen(screen)
for line in data:

    line = line.strip()
    # print(line, current_cycle, register_value)
    command = line.split(" ")[0]


    if(command == "addx"):
        to_add = int(line.split(" ")[1])
        for i in range(2):
            draw(current_cycle - 1, register_value)
            current_cycle += 1

        register_value += to_add

    elif(command == "noop"):
        draw(current_cycle - 1, register_value)
        current_cycle += 1
        continue

    else:
        raise Exception("Unknown Command")


#print_screen(screen)
        

