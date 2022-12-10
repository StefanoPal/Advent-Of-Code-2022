with open("inputd6.txt", "r") as f:
    data = f.readline()

offset = 14
for i, char in enumerate(list(data)[offset - 1:]):
    print(set(data[i - offset : i]))
    if (len(set(data[i - offset : i])) == offset):
        print(i)
        break