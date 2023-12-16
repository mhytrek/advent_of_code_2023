def change(sym, sum):
    sum += ord(sym)
    sum *= 17
    sum = sum % 256
    return sum

def split(str):
    label= ""
    focal=""
    for i in range(len(str)):
        if str[i].isalpha():
            label += str[i]
        elif str[i].isnumeric():
            focal += str[i]
        else:
            cmp = str[i]
    return label, cmp, focal


def bokk_hash(line):
    boxes ={}
    input = line[0][:-1].split(",")
    result  = 0
    for string in input:
        l,c,f = split(string)
        sum = 0
        for char in l:
            sum = change(char,sum)
        box = boxes.get(sum)
        if c == "-" and box != None:
            for i in range(len(box)):
                if box[i][0] == l:
                    box.pop(i)
                    boxes[sum] = box
                    break
        elif c == "=":
            flag = True
            if box != None:
                for i in range(len(box)):
                    if box[i][0] == l:
                        box[i] = [l,f]
                        flag = False
                if flag:
                    box.append([l,f])
            else:
                box = [[l,f]]
            boxes[sum] = box

    for i in range(256):
        box = boxes.get(i)
        if box != None:
            for j in range(len(box)):
                result += (i+1) * int(box[j][1]) * (j+1)
    return result

file = open("example_15.txt")
lines = file.readlines()
print(bokk_hash(lines))