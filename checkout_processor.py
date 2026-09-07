from functools import reduce

prices=[100,200,300,400,500]

filtered_prices = list(filter(lambda price: price >= 200, prices))

prices_with_tax = list(map(lambda price: price*1.2, filtered_prices))

total_receipt = reduce(lambda a, b: a + b, prices_with_tax,0)

print(f"Items to process: {filtered_prices}")
print(f"Prices with tax: {prices_with_tax}")
print(f"Total Receipt: {total_receipt}")
