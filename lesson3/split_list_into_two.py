# [1, 2, 3, 4, 5, 6]
# [1, 2, 3]
# [1, 2, 3, 4, 5]
# [1]
# []

num_list = []
z = len(num_list)

if z % 2 == 0:
    num_list = [num_list[: z // 2]] + [num_list[z // 2 :]]
elif z % 2 != 0:
    num_list = [num_list[: (z + 1) // 2]] + [num_list[(z + 1) // 2 :]]
elif z == 1:
    num_list = [
        [][num_list[0]],
    ]
else:
    num_list = [[][num_list[0]]]

print(num_list)
