def minimaxi(arr):
    mini = arr[0]
    maxi = arr[0]
    sum = 0

    for i in range(len(arr)):
        sum = sum + arr[i]

        if(arr[i]>maxi):
            maxi = arr[i]
        elif(arr[i]<mini):
            mini = arr[i]
    #mini = min(arr)
    #maxi = max(arr)

    sum1 = sum - mini
    sum2 = sum - maxi

    print(f"MAXIMUM : {sum1}\nMINIMUM : {sum2}")

arr = [1 , 3 , 5 , 7 , 9]
minimaxi(arr)


        