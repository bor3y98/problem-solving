def insertion_sort(num_list):
    if len(num_list) <= 1:
        return num_list
    counter_1 = 1
    while counter_1 < len(num_list):
        counter_2 = counter_1
        temp_value = num_list[counter_1]
        while counter_2 > 0:
            if temp_value < num_list[counter_2 - 1]:
                num_list[counter_2] = num_list[counter_2 - 1]
                counter_2 -= 1
            else:
                num_list[counter_2] = temp_value
                temp_value = None
                break
        if temp_value:
            num_list[0] = temp_value
        counter_1 += 1
    return num_list