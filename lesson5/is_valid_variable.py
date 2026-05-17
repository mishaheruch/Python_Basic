import string
import keyword

z = str(input("Введіть назву зміної:"))

for char in string.punctuation + " ":
    if char == "_":
        continue
    elif char in z:
        print("False")
        exit()
for x in z:
    if not x.isalpha():
        continue
    if x.isupper():
        print("False")
        exit()
if z == "_":
    print("True")
    exit()
elif z[0].isdigit():
    print("False")
    exit()
elif "__" in z:
    print("False")
    exit()
else:
    if z not in keyword.kwlist:
        print("True")
    else:
        print("False")
        exit()
