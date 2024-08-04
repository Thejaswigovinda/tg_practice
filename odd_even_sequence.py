new_list = [3,8,9,7,4,5,6]
even_list =[]
odd_list = []
for item in new_list:
    if item%2==0:
        even_list.append(item)
    else:
        odd_list.append(item)
even_list.sort()
odd_list.sort()
print(even_list)
print(odd_list)

odd_list.extend(even_list)
print(odd_list)

