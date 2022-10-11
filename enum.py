def my_enum(it):
    ls = []
    for i in range(len(it)):
        ls.append((i, it[i]))
    return ls

it = [1,2,3]

for key, value in my_enum(it):
    print(key, value)
