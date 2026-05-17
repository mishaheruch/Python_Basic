# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True

import string
import keyword

z = str(input())

if z[0].isdigit():
    print("false")
    exit()
elif not z.count("_") != 1:
    if not z.islower():
        print("false")
        exit()
elif "__" in z:
    print("false")
    exit()

for char in string.punctuation:
    if char == "_":
        continue
    elif char in z:
        print("false")
        exit()
print(z not in keyword.kwlist)
