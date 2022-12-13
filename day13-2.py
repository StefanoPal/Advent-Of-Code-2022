import ast
with open("inputd13.txt", "r") as f:
    data = f.read().split("\n\n")
    packets = []
    for line in data:
        packets.append(line.split("\n")[0])
        packets.append(line.split("\n")[1])

    packets.append("[[2]]")
    packets.append("[[6]]")

    packets = [ast.literal_eval(packet) for packet in packets]


def run_check(left: int | list, right: int | list) -> bool | None:

    if(isinstance(left, int) and isinstance(right, int)):

        if(left == right):
            return None
        
        if(left > right):
            return False
        else:
            return True

    if((isinstance(left, int) and isinstance(right, list))):
        left = [left]

    if((isinstance(left, list) and isinstance(right, int))):
        right = [right]

    if(isinstance(left, list) and isinstance(right, list)):
        for i in bigger_list_range(left, right):

            try:
                res = run_check(left[i], right[i])

                if(isinstance(res, bool)):
                    return res
                

            except IndexError:

                if(len(right) == len(left)):
                    return True

                if(len(right) > len(left)):
                    return True
                else:
                    return False

        return None

    raise Exception("Error")

def bigger_list_range(one: list, two: list) -> range:
    return range(max(len(one), len(two)))

results = []
for i, _ in enumerate(packets[:-1]):
    for j in range(i, -1, -1):
        #print(j)
        if(not run_check(packets[j], packets[j + 1])):
            packets[j], packets[j + 1] = packets[j + 1], packets[j]
        else:
            break



first_id = 0
second_id = 0
for i, elem in enumerate(packets[1:]):

    if(str(elem) == "[[2]]"):
        first_id = i + 1
        continue

    if(str(elem) == "[[6]]"):
        second_id = i + 1
        continue


# [print(packet) for packet in packets]
print(first_id + 1, second_id + 1, (first_id + 1) * (second_id + 1))

