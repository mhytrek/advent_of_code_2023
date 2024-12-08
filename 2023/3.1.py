import get_input

example = ["467..114..",
"...*......",
"..35..633.",
"......#...",
"617*......",
".....+.58.",
"..592.....",
"......755.",
"...$.*....",
".664.598.."]

def do_frame(tabel):
    new_tabel = [["." if ((i == 0) or (j==0) or (i==len(tabel)+1) or  (j==len(tabel)+1)) else tabel[i-1][j-1] for j in range(len(tabel[0])+1)] for i in range(len(tabel)+2)]
    return new_tabel

def is_symbol_adjacent(new_tabel,i,j):
    for a in [-1,1,0]:
        for b in [-1,1,0]:
            to_check = new_tabel[i+a][j+b]
            if (not to_check.isnumeric()) and to_check != "." and to_check != "\n":
                return True
    return False

def sum(tabel):
    sum = 0
    new_tabel = do_frame(tabel)
    print(new_tabel)
    for r in range(1,len(new_tabel)-1):
        num = 0
        flag = False
        for c in range(1,len(new_tabel[0])-1):
            if new_tabel[r][c].isnumeric():
                if num != 0:
                    num *= 10
                num += int(new_tabel[r][c])
                if is_symbol_adjacent(new_tabel,r,c):
                    # print(num)
                    flag = True
            else:
                if flag == True:
                    sum += num
                num = 0
                flag = False
        if flag != False:
            sum += num
    return sum

if __name__ == '__main__':
    lines = get_input.download_input(3)
    print(lines)
    print(sum(lines))
    # print(sum(example))



