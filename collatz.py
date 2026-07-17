def collatz(n):

    while n!=1:
        print(n , end=" ")
        if(n%2 == 0):
            n = n//2
        elif n%2==1:
            n = n*3 + 1
    print(n , end=" ")
    

    return n

n = 10
collatz(n)
    
