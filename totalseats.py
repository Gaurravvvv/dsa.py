def seat(arr):
    cnt=0
    for i in range(len(arr)):
        if arr[i]==0:
            cnt+=1
    
    return cnt

arr=[]
n = int(input("Num : "))
for i in range(n):
    num = int(input("Add Num:"))
    arr.append(num)

print(arr)

print("Total Empty Seats : " , seat(arr))