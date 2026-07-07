def calculate_final_price(items_list, discount_code):
    total_sum = sum(items_list)
    
    if discount_code == "SAVE10":
        return total_sum * 0.9
    elif discount_code == "SAVE20":
        return total_sum * 0.8
    else:
        return total_sum

cart = []
print("--- Welcome to the Store ---")
while True:
    price = input("Enter item price (or type 'done' to finish): ")
    if price.lower() == 'done':
        break
    cart.append(float(price))

code = input("Enter discount code (leave blank if none): ")

final_price = calculate_final_price(cart, code)
print(f"The final price after discount is: {final_price}")
