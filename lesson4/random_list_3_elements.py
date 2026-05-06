import random

number = []

for i in range(random.randint(3, 10)):
    number.append(random.randint(1, 10))

result = [number[0], number[2], number[-2]]

print(result)
