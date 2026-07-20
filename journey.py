def journey(n1 , hr , n2 , total):
    if(hr*60<=total):
        fcost = n1*hr
        rem = total - (hr*60)
        remhr = ceil(rem/60)

        lcost = remhr*n2

        #print(remhr)

        return fcost+lcost
    else:
        total = ceil(total/60)
        return total*n1


def ceil(n):
    return int(-(-n//1))



n1 =  20
hr = 4
n2 =  40
total = 30

print("Total Cost : " , journey(n1 , hr , n2 , total))

nn1 = 30 
hhr = 5
nn2 = 35 
ttotal = 500

print("Total Cost : " , journey(nn1 , hhr , nn2 , ttotal))