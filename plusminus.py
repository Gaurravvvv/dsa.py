def plusminus(arr):
    pos = 0
    neg = 0
    neu = 0
    for i in range(len(arr)):
        if arr[i]>0:
            pos+=1
        elif arr[i]<0:
            neg+=1
        else :
            neu+=0
    
    print(f"{pos/len(arr):.6f} \n{neg/len(arr):.6f} \n{neu/len(arr):.6f}")

arr = []
n = int(input("Size : "))
for i in range(n):
    num = int(input("Incoming Rated Capacity : "))
    arr.append(num)

plusminus(arr)



