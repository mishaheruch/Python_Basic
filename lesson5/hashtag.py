import string

my_string = input("Введіт речення: ")

my_string = my_string.title()
my_string = my_string.replace(" ", "")

for x in string.punctuation:
    my_string = my_string.replace(x, "")

print("#" + my_string[:139])
