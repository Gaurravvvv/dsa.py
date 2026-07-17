arrsize=int(input())
arr=[]
for i in range(arrsize):
    elt=int(input())
    arr.append(elt)

i=0
for j in range(len(arr)):
    if arr[j]!=0:
        temp=arr[j]
        arr[j]=arr[i]
        arr[i]=temp
        i+=1

print(arr)        
