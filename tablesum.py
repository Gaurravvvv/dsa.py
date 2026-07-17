def tablesum(n):
    sum = 0
    for i in range(11):
        sum = sum + n*i


    return sum    #o(n)

def table(n):
    return n*55

n = int(input("Num : "))
print("Sum O(n): " , tablesum(n))
print("Sum O(1) : " , table(n))
