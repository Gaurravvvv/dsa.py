arr=[[11,2,4],
     [4,5,6],
     [10,8,-12]]
sum=0
sum1=0
i=0
for j in range(len(arr)):
    sum+=arr[i][j]
    print(sum)

    sum1+=arr[i][len(arr)-1-i]
          
    print(sum1) 
    i+=1

diff=sum-sum1
print(diff)