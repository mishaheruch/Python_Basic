first_number = float(input("Введіт перше число : "))
second_number = float(input("Введіт друге число : "))

operation = input("Вибиріть знак(+, -, *, /): ")

if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number
elif operation == "/":
    if second_number == 0:
        print("Діленя на 0 не можливе")
        exit()
    result = first_number / second_number
else:
    result = 0
    print("Невідомий оператор")

print("Результат:", result)
