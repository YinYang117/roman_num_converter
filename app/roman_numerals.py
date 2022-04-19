def parse(string):
    num_list = []
    for char in string:
        if char == "I":
            num_list.append(1)
        elif char == "V":
            num_list.append(5)
    i = 0
    while i < len(num_list):
        if i < (len(num_list) - 1):
            if num_list[i] < num_list[i + 1]:
                num_list[i] *= -1
        i += 1
    return sum(num_list)