def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        return price

#  user for input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculating final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percent)

# printing final price or original price
if final_price != original_price:
    print("Final price after discount:", final_price)
else:
    print("No discount applied. Original price:", original_price)
  