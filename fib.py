n = int(input("Enter a number: "))
a = 0
b = 1

for i in range(n) : 
    c = a + b
    a = b
    b = c

print(f"the n-th fibonacci number is {a} ")
