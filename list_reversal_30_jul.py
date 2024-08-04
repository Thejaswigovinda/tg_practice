def reverse_list(new_list):
    reversed_list = []
    while len(new_list)>0:
        reversed_list.append(new_list[-1])
        new_list.pop(-1)
    print(reversed_list)


data_list = [1,2,3,4,5]
reverse_list(data_list)