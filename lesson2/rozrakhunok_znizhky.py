price = int(input("Введіть ціну: "))
discount_percent = int(input("Введіть відсоток знижки: "))

discounted_price = price - price * discount_percent / 100
print("Ціна зі знижкою:", int(discounted_price))
