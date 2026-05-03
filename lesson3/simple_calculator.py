first_number = int(input("Введіт перше число : "))
second_number = int(input("Введіт друге число : "))

operation = input("Вибиріть знак(+, -, *, /): ")

if operation == "+":
    result = first_number + second_number
    print("Результат:", result)
elif operation == "-":
    result = first_number - second_number
    print("Результат:", result)
elif operation == "*":
    result = first_number * second_number
    print("Результат:", result)
elif operation == "/":
    if first_number == 0:
        print("Діленя на 0 не можливе")
        exit()
    result = first_number / second_number
    print("Результат:", result)
else:
    print("Невідомий оператор")
