def sort012(arr):

    left = 0 
    mid = 0
    right = len(arr)-1

    #for left in range(len(arr)):
    while mid<=right:
        if arr[mid]==2:
            arr[mid] , arr[right] = arr[right] , arr[mid]
            right-=1
            #mid+=1
        elif arr[mid]==0:
            arr[mid] , arr[left] = arr[left] , arr[mid]
            mid+=1
            left+=1
        else:
            mid+=1
            
    return arr


arr= [2 , 1 , 0 , 1 , 0 , 2 , 2 , 1 , 0 , 1]

# n = int(input("Size : "))

# for left in range(n):
#     num1 = int(input("Num : "))
#     arr.append(num1)

print(sort012(arr))


        
