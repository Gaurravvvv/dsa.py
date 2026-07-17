def balance(arr1 , arr2 , r):
    sum1 = 0
    sum2 = 0
    for i in range(len(arr1)):
        sum1 = sum1 + arr1[i]
    for i in range(len(arr2)):
        sum2 = sum2+arr2[i]

    sum1 = sum1 - len(arr1)*r
    sum2 = sum2 - len(arr2)*r

    if sum1 == sum2:
        return "BALANCED"
    
    if sum1>sum2:
        return ((sum1-sum2)+r)*-1
    else:
        return (sum2-sum1)+r
    
arr1 = []
arr2 = []
n1 = int(input("No . of Incoming pipes : "))
n2 = int(input("No . of Outgoing Pipes :"))

r = int(input("Rust Factor : "))

for i in range(n1):
    num1 = int(input("Incoming Rated Capacity : "))
    arr1.append(num1)
for i in range(n2):
    num2 = int(input("Outgoing Rated Capacity : "))
    arr2.append(num2)


print("Answer : " , balance(arr1 , arr2 , r))