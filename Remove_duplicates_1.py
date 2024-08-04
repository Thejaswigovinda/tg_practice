data = [1,2,3,4,3,4,1]
new_list = []
new_index =[]
def remove_duplicates(iterable):
    for index, value in enumerate(iterable):
        if value not in new_list:
            new_list.append(value)

        else:
            new_index.append(index)
    print(new_index)
    print(new_list)

remove_duplicates(data)