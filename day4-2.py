with open("inputd4.txt", "r") as f:
    data = f.readlines()

def get_range(range_string):
    return range(int(range_string.split("-")[0]), int(range_string.split("-")[1]) + 1) 

total = 0
for line in data:
    first_range, second_range = line.strip().split(",")
    first_range = get_range(first_range)
    second_range = get_range(second_range)

    if(any(i in second_range for i in first_range)):
        total += 1

print(total)