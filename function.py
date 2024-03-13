    # funtion define
def calculate_discount():
    price = float(input("Enter the price:  "))
    discount_percent = int(input("Enter the percentage: "))

        #new_price
        # local variable
    if  discount_percent >= 20:
        discount_percent = discount_percent / 100
        discount = discount_percent * price
        new_price = price - discount
        print("The  discounted price is " + str(discount_percent))
        print("The new price is " + str(new_price))
    else:
        print(f"The percentage {discount_percent} % is too low, the {price} is the original. Thank you!!!")

calculate_discount()