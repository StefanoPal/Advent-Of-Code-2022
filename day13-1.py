import ast
with open("inputd13.txt", "r") as f:
    packets = f.read().split("\n\n")


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
for packet in packets:
    print(len(packets))
    first, second = packet.split("\n")
    first = ast.literal_eval(first)
    second = ast.literal_eval(second)

    # first = [1,1,3,1,1]
    # second = [1,1,5,1,1]

    results.append(run_check(first, second))


print([i + 1 for i, elem in enumerate(results) if elem == True])
print(sum([i + 1 for i, elem in enumerate(results) if elem == True]))