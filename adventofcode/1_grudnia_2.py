import get_input

word_to_digit = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}
def calibration_value(line: list)-> int:
    p = 0
    k = 0
    global word_to_digit
    for i in range(len(line)):

        if line[i].isnumeric():
            p = int(line[i])
            break

        for j in range(i+1,len(line)+1):
            word = word_to_digit.get(line[i:j])
            if word != None:
                p = word
                break

        if p != 0:
            break

    for i in range(len(line)-1, -1, -1):

        if line[i].isnumeric():
            k = int(line[i])
            break

        for j in range(0,i):
            word = word_to_digit.get(line[j:i+1])
            if word != None:
                k = word
                break

        if k != 0:
            break

    return p*10 + k

def find_all_values(input:list) -> int:
    s = 0
    for i in range(len(input)):
        s += calibration_value(input[i])
    return s

if __name__ == '__main__':
    input = get_input.download_input(1)
    print(find_all_values(input))