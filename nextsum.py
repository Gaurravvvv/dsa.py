def nextsum(arr , n):
    summ = sum(arr)
    for i in range(n):
        temp = arr[i]
        arr[i] = summ - arr[i]
        summ = summ - temp

   

    return arr

arr = [10 , 20 , 30 , 40 , 50]
n = len(arr)

print(nextsum(arr , n))
        

    