# def fib(n):
#     first = 0
#     second = 1
#     temp = 0
#     res = first+second
#     print(first)
#     print(second)
#     while res<=n:
#         print(res)
#         temp = res
#         res = second + res
#         second = temp



# fib(10)

def fib(n):
    first = 0
    second = 1
    temp = 1
    res = second
    sum=first+second
    cnt=2
    print(first)
    print(second)
    while cnt<n:
        print(res)
        temp = res
        res = second + first
        first=second
        second=res

        sum+=res
        cnt+=1
    print(res)

    return sum



print(fib(8))
        
