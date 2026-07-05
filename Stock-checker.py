stock=["Apple","Banna","Milk","Bread","Chocolate","Water"]

product_name=input("Please,Enter the name of the product")

for i in stock:

  if i== product_name:
    print("Yes we have "+product_name+" in stock")
    break

else:
    print("Sorry, we don't have "+product_name+" in stock")
