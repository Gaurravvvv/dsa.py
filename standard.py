import math
def standard(arr , n):
    m = mean(arr)
    sum = 0
    for i in range(len(arr)):
        arr[i] = arr[i]-m
        arr[i] = arr[i]*arr[i]

    for i in range(len(arr)):
        sum = arr[i]+sum

        
    return math.sqrt((sum)/n)

def mean(arr):
    avg = 0
    for i in range(len(arr)):
        avg = arr[i]+avg
    return avg/len(arr)



arr = [ 3 , 8 , 4 , 2 , 5 , 6 ,7]
arr1=[10 , 15 , 17]
n1 = len(arr1)
n = len(arr)

print(f"{standard(arr , n):.2f}")
print(f"{standard(arr1 , n1):.2f}")
