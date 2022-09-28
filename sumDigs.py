number = int(input("Enter a number: "))
summ = 0

while number != 0:
    summ += number % 10
    number //= 10



print(int(summ))

