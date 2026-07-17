def efficiency(arr , n):
    m = 0 
    sum = 1
    low = 0
    while n <= len(arr)-1:
        for i in range(n):
            sum = sum*arr[i]
            m = max(m , sum)

        n+=1
        low += 1 # 3 -2 -8 4 1

arr = []
n = int(input("Employeee Eff : "))
n1 = int(input("Size : "))
for i in range(n1):
    num = int(input("Nums : "))
    arr.append(num)

print("Ans : " , efficiency(arr , n) )


    