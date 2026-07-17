arrsize=int(input())
arr=[]
for i in range(arrsize):
    elt=int(input())
    arr.append(elt)
print(arr)
for i in range (len(arr)):
    for j in range(i+1):    
        if arr[j]==0:
            temp=arr[j]
            arr[j]=arr[i]
            arr[i]=temp

print(arr)