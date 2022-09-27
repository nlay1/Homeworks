sumDiv = 0

for number in range(10001):
    for i in range(1, number):
        if number % i == 0:
            sumDiv = i + sumDiv
        if sumDiv == number:
            print(f"{number} is perfect number")
