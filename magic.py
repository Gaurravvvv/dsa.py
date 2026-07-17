def magic(x,n):
    result=0
    power=0
    while(x!=0):
        digit=(x%10)
        newdigit=(digit+n)%10
        result+=newdigit * (10**power)
        power+=1
        x = x//10
    return result

print(magic(328,3))    
