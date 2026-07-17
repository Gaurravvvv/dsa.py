def palin(str , n):
    # if str[::-1] == str:
    #     return 1 

    left = 0 
    right = len(str)-1
    while left<right:

        if(str[left]==str[right]):
            left+=1
            right-=1 
        else:
            return 0
    return 1
    
str = input("Enter Str : ")
n = len(str)

if palin(str , n)==1:
    print("Is Palindrome")
else:
    print("not a Palindrome")