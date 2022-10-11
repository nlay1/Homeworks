def is_sorted(ls):
    ls_sort = ls.copy()
    ls_sort = ls_sort.sort()
    if ls == ls_sort:
        return True
    else:
        return False

ls = [1,2,4]
x = is_sorted(ls)
print(x)
