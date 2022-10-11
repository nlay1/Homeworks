def merge(arr1, arr2):
    arr3 = [0]*(len(arr1)+len(arr2))
    i, j, k = 0, 0, 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            k += 1
            i += 1
        else:
            arr3[k] = arr2[j]
            k += 1
            j += 1
            
    while i < len(arr1):
        arr3[k] = arr1[i];
        k += 1
        i += 1
        
    while j < len(arr2):
        arr3[k] = arr2[j];
        k += 1
        j += 1
    
    return arr3

ls1 = [1,3,5,7]
ls2 = [2,4,6,8,10]
ls3 = merge(ls1,ls2)
print(ls3)
