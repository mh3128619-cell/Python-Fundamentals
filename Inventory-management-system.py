inventory_count = 50
threshold = 10

def sell_product(quantity):
    global inventory_count
    
    if quantity > inventory_count:
        print("Error: Requested quantity is greater than available stock!")
    else:
        inventory_count -= quantity
        if inventory_count <= threshold:
            print(f"Warning: Low stock! Remaining quantity is {inventory_count}")
        else:
            print(f"Sale successful, remaining in stock: {inventory_count}")

sell_product(20)
sell_product(25)
sell_product(10)
