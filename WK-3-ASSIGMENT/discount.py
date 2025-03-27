def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        new_price= price - (price * discount_percent/100)
        print(new_price)

    else: print(price)


price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

calculate_discount(price, discount_percent)