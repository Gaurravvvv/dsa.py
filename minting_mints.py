def mints(n,len):
    sum = n
    for i in range(1,len):
        sum += sum-1 #previous = sum-1 , sum = sum + previous
    return sum

#print(mints(4,1)) 
num = int(input(""))
length = int(input(""))
if length >=1 and length < 20 and num > 2 and num < 10 :
    print(mints(num,length))
else:
    print("Error..........")    
  