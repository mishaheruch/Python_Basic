# [1, 3, 5] => 30
# [6] => 36
# [] => 0
# [0, 1, 7, 2, 4, 8] => (0 + 7 + 4) * 8 = 88

numbers = [0, 1, 7, 2, 4, 8]

if len(numbers) == 0:
    print(0)
    exit()
else:
    res = 0
    for i in range(len(numbers)):
        if i % 2 == 0:
            res += numbers[i]

print(res * numbers[-1])
