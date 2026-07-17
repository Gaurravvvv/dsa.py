numofinteriorwall=int(input())
numofexteriorwall=int(input())
sum=0
for i in range(numofinteriorwall):
    surfacearea=float(input())*18
    sum+=surfacearea
    

for i in range(numofexteriorwall):
    exsurfacearea=float(input())*12
    sum+=exsurfacearea


if numofinteriorwall==0 and numofexteriorwall==0:
    print("Don't want to paint")


print("Total Estimated Cost :" ,sum ,"INR")