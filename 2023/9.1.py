import get_input

def diffrence_tabel(tab):
    new = []
    for i in range(0,len(tab)-1):
        new.append(tab[i+1]-tab[i])
    return new

def all_Zeros(tab):
    if set(tab) == {0}:
        return True
    else:
        return False

def predict(lines):
    sum = 0
    for line in lines:
        num = line[:-1].split(" ")
        num = [int(num[i]) for i in range(len(num))]
        tabels = []
        new = num
        while not all_Zeros(new):
            tabels.append(new)
            new = diffrence_tabel(new)
        predicted = 0
        for j in range(len(tabels)):
            predicted += tabels[j][-1]
        sum += predicted
    return sum

lines = get_input.download_input(9)
# file = open("example_9.txt")
# lines = file.readlines()
print(predict(lines))
