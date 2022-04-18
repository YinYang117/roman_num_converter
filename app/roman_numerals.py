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
    

    # i = 0
    # while i < len(string):
    #     if string[i] == "I":
    #         i_counter += 1
    #     elif string[i] == "V":
    #         v_counter += 1

    #         shorthand = True
    #     i += 1
        
    # if shorthand == False:  
    #     return i_counter + 5 * v_counter
    # else:
    #     print("all the stuff", shorthand, i_counter, v_counter)
    #     return i_counter - 5 * v_counter