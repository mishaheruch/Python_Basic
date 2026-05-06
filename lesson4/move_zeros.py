#
# [0, 1, 0, 12, 3] -> [1, 12, 3, 0, 0]
# [0] -> [0]
# [1, 0, 13, 0, 0, 0, 5] -> [1, 13, 5, 0, 0, 0, 0]
# [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]

number = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

zero_count = number.count(0)

for i in range(zero_count):
    zero_index = number.index(0)
    number.pop(zero_index)
    number.append(zero_count * 0)

print(number)
