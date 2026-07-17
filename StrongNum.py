
def fact(num):
    if num == 1:
        return 1
    else :
        return num*fact(num-1)
 
 
num = int(input())
original_num = num
summ = 0
while(num != 0):
    digit = num % 10
    summ+= fact(digit)
    num = num//10
        
if summ == original_num:
    print("Yes")
