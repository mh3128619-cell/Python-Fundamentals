from functools import reduce

cart = [120, 50, 80, 200, 30]

filtered_cart = list(filter(lambda price: price >= 50, cart))

prices_with_tax = list(map(lambda price: price + 10, filtered_cart))

total_receipt = reduce(lambda a, b: a + b, prices_with_tax)

print(f"Items to process: {filtered_cart}")
print(f"Prices with tax: {prices_with_tax}")
print(f"Total Receipt: {total_receipt}")
