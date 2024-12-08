import Input_helper

def parse_data(lines):
    data_1 = [line.replace('\n', '').split("|") for line in lines]
    rules = [list(map(int,line)) for line in data_1 if len(line) > 1]

    data_2 = [line.replace('\n', '').split(",") for line in lines]
    list_print = [list(map(int,line)) for line in data_2 if len(line) > 1]
    return rules, list_print

def create_dict(rules):
    dict = {}
    for rule in rules:
        if dict.get(rule[0]) is None:
            dict[rule[0]] = {rule[1]}
        else:
            dict[rule[0]].add(rule[1])
    return dict

def check_order(order, rules):
    for i in range(len(order)):
        not_before = rules.get(order[i])
        if not_before is not None and len(not_before.intersection(set(order[0:i]))) > 0:
            return False
    return True

def check_before(orders, dict):
    sum = 0
    for order in orders:
        if check_order(order, dict):
            print(order[len(order)//2])
            sum += order[len(order)//2]
    return sum



def main():
    get_input.get_input(5)
    file = open("input_day_5", "r")
    lines = file.readlines()
    rules, order = parse_data(lines)
    dict = create_dict(rules)
    print(order)
    return check_before(order, dict)



if __name__ == "__main__":
    print(main())