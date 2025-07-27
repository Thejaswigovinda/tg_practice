def swap_tuple(new_tuple, index1, index2):
    new_tuples = list(new_tuple)
    new_tuples[index1], new_tuples[index2] = new_tuples[index2], new_tuples[index1]
    print(tuple(new_tuples))

tuples = (1,2,3,4,5)
index1 = 2
index2 = 3
print(index2)
swap_tuple(tuples, index1, index2)