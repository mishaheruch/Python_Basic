num = int(input("Enter a number: "))

while num > 9:
    x = 1
    for i in str(num):
        x *= int(i)
    num = x

print(num)
