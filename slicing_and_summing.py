def sum_slices(my_list):
    new_list = my_list[:3]
    value = 0
    for item in new_list:
        value = value + item
    print(value)

data = [2,3,4,5,6,7]

sum_slices(data)