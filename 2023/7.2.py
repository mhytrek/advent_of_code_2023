import get_input
def war(hand):
    cards = {"A":0, "K":1, "Q":2, "T":4, "9":5, "8":6, "7":7, "6":8, "5":9, "4":10, "3":11, "2":12, "J":13}
    dic = {}
    m = 0
    for card in hand:
        if dic.get(card) != None:
            dic[card] += 1
            if card != "J":
                m = max(m,dic[card])
        else:
            dic[card] = 1
            if card != "J":
                m = max(m, dic[card])
    if dic.get("J") != None and len(dic.keys()) != 1:
        a = len(dic.keys())-1
        b = -(m+dic.get("J"))
    else:
        a = len(dic.keys())
        b = -m
    c = [cards[hand[i]] for i in range(len(hand))]
    return (a,b,c)

def play(lines):
    lines = [lines[i][:-1].split(" ")[0:2] for i in range(len(lines))]
    lines.sort(key=lambda x: war(x[0]), reverse = True)
    sum = 0
    i=1
    for j in range(len(lines)):
        sum += int(lines[j][1])*i
        i += 1
    print(sum)

# lines = get_input.download_input(7)
file = open("input_day_7")
lines = file.readlines()
play(lines)
print(250865404)



