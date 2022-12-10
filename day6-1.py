with open("inputd6.txt", "r") as f:
    data = f.readline()


for i, char in enumerate(list(data)[3:]):
    print(set(data[i - 4 : i]))
    if (len(set(data[i - 4 : i])) == 4):
        print(i)
        break
