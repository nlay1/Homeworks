L=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

ls = [L[i+1] - L[i] for i in range(len(L) - 1) ]

print(ls)
print(max(ls))

percentage = ls.count(2) / 100
print(percentage)    
