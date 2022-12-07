with open("inputd4.txt", "r") as f:
    data = f.readlines()

def get_range(range_string):
    return range(int(range_string.split("-")[0]), int(range_string.split("-")[1]) + 1) 

total = 0
for line in data:
    first_range, second_range = line.strip().split(",")
    first_range = set(get_range(first_range))
    second_range = set(get_range(second_range))

    if(first_range.issubset(second_range) or second_range.issubset(first_range)):
        total += 1

print(total)