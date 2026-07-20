def pro(arr):
    product = 1
    for i in range(len(arr)):
        if arr[i]==0:
            continue
        product = arr[i]*product
    

    for i in range(len(arr)):
        if arr[i]==0:
            continue
        arr[i]=product//arr[i]

    return arr


arr = [ 2 , 3 , 0 , 5]
arr1 = [4 , 6 , 5]

print("Answer Arr : " , pro(arr))
print("Answer Arr : " , pro(arr1))
