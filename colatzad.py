def collatz(n):
    a = 0
    while n!=1:
        a+=1
        #print(n , end=" ")
        if(n%2 == 0):
            n = n//2
        elif n%2==1:
            n = n*3 + 1
    #print(n , end=" ")
    a+=1
    

    return a


def counter( i , j):
    ans =0
    while i<=j:
        ans = max(ans , collatz(i))
        i=i+1

    return ans 

i = int(input("Num 1 : "))
j = int(input("Num 2 : "))
print(f"{i} {j} {counter(i , j)}")


