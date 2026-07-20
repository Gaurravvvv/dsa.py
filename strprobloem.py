def conversion(str):
    str = str.upper()
    sum = 0
    if str:
        for i in str: 
            if i=="A":
                sum+=1
            elif i=="B":
                sum+=10
            elif i=="C":
                sum+=100
            elif i=="D":
                sum+=1000
            elif i=="E":
                sum+=10000
            elif i=="F":
                sum+=100000
            elif i=="G":
                sum+=1000000
            else:
                sum+=0
    
        return sum
    else:
        return 0

str = input("Enter Str : ")
print("Sum : " , conversion(str))
