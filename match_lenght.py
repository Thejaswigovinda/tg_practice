listin = [['t','h','e','j','a','s','w','i'], ['g','o','v','i','n','d','a'], ['p','y','t','h','o','n']]

First_name = len(listin[0])
print(First_name)

for inside_list in listin:
    while len(inside_list) < First_name:
        inside_list.append('*')
print(listin)