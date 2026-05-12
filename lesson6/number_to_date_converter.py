num = int(input("Please enter a number: "))

if num < 0 or num >= 8640000:
    print("Please enter a valid number")
else:
    a, num = divmod(num, 24 * 60 * 60)
    b, num = divmod(num, 60 * 60)
    c, num = divmod(num, 60)

    if 11 <= a <= 19:
        day = "днів"
    elif a % 10 == 1:
        day = "день"
    elif 2 <= a % 10 <= 4:
        day = "дні"
    else:
        day = "днів"

    print(f"{a} {day}, {str(b).zfill(2)}:{str(c).zfill(2)}:{str(num).zfill(2)}")
