# num_list = [12, 3, 4, 10]
# num_list = [1]
# num_list = []
num_list = [12, 3, 4, 10, 8]

if len(num_list) > 1:
    last = num_list.pop()
    num_list.insert(0, last)

print(num_list)
