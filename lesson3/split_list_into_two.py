# [1, 2, 3, 4, 5, 6]
# [1, 2, 3]
# [1, 2, 3, 4, 5]
# [1]
# []

num_list = [1, 2, 3]
z = len(num_list)

if z == 1:
    num_list = [
        [][num_list[0]],
    ]
    print(num_list)
elif z == 0:
    num_list = [[][num_list[0]]]
    print(num_list)

else:
    first_part = num_list[: (z + 1) // 2]
    second_part = num_list[(z + 1) // 2 :]
    result = [first_part, second_part]
    print(result)

# num_list = [1]
#
# z = len(num_list)
#
# first_part = num_list[: (z + 1) // 2]
# second_part = num_list[(z + 1) // 2 :]
#
# result = [first_part, second_part]
#
# print(result)
