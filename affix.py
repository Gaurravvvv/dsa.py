def affix(m , n):

    for i in range(m , n+1):
        if n<=99:
            if(i>=10 and i<=99):
                print(i , end=" ")
            else:
                print(f"0{i}" , end=" ")
            #m+=1
        if n<=999 and n>99:
            if(i>=100 and i<=999):
                print(i , end=" ")
            elif i>=10 and i<=99:
                print(f"0{i}" , end=" ")
            else:
                print(f"00{i}" , end=" ")
            #m+=1



        

m = int(input("Enter num 1 : "))
n = int(input("Enter Num 2 : "))

affix(m , n)