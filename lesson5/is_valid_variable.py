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

z = "asserT"

if z[0].isdigit():
    print("false")
    exit()

y = z.islower

if not z.isalpha():
    print("false")
    exit()

if z in string.punctuation:
    print("Please, use only letters and numbers")
    exit()


print(z)
print(y)
print(keyword.iskeyword)
