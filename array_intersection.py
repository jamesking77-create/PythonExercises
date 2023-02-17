two_d_array = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]
result_list = []


def intersect_array():
    for j in two_d_array[0]:
        if j in two_d_array[1] and j in two_d_array[2]:
            result_list.append(j)
    print(result_list)


print(intersect_array())
