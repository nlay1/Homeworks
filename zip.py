def my_zip(it1, it2):
    return [(it1[i], it2[i]) for i in range(len(it1)) if len(it1) == len(it2)]

tuple1 = (1,2,3)
tuple2 = (4,5,6)

x = my_zip(tuple1, tuple2)
print(x)
