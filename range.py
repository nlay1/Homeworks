def my_range(stop):
    ls = []
    i = 0
    while i < stop:
        ls.append(i)
        i += 1 
    return ls

for i in my_range(10):
    print(i, end = ' ')
