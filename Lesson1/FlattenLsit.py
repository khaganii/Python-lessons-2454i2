flatten = [[1, 2, [3, [[3,9], 8] , 4]], [5, 6], 7]
new_list = []
#1, 2, [3, [3,9]], 8 - > 1, 2, 3, 3, 9, 8
#3, [3,9]  - > 3, 3, 9
# 3, 9
def clearing(el):
    empty_list = []
    for i in el:
        if isinstance(i, list):
            empty_list.extend(clearing(i))
        else:
            empty_list.append(i)
    return empty_list

for el in flatten:
    if isinstance(el, list):
        new_list.extend(clearing(el))
    else:
        new_list.append(el)

print(new_list)

#[1, 2, [3, [[3,9], 8] , 4]], [5, 6], 7
#1, 2, [3, 4], 5, 6, 7