prod = {}
for i in range(10): 
    name=input("Enter the name of product: ")
    prod[name] = int(input("Enter the price: "))


print(prod)

while True:
    name = input("Enter product name to check for price or 0 to exit: ")
    if name == '0':
        break
    else:
        if name in prod:
            print(prod[name])
        else:
            print("Not available")

