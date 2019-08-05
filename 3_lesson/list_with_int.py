def sort_int_list(list):
    for item in list:
        if not isinstance(item, int):
            raise ValueError
    sorted_list = sorted(list)
    return sorted_list

list = [1,6.0,6]

print(sort_int_list(list))
            
        