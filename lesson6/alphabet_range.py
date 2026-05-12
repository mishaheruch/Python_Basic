import string

input_string = str(input("Введіть букви: "))

x = input_string[0]
y = input_string[-1]

x = string.ascii_letters.index(x)
y = string.ascii_letters.index(y)

print(string.ascii_letters[x : y + 1])
