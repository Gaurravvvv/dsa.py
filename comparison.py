def comparison(arr1 , arr2):
    alice = 0
    bob = 0
    for i in range(len(arr1)):
        if arr1[i]>arr2[i]:
            alice+=1
        elif arr1[i]<arr2[i]:
            bob+=1
        else:
            continue
    
    ans = []
    ans.append(alice)
    ans.append(bob)

    print(ans)

arr1 = [5 , 6 , 7]
arr2 = [3 , 5 , 6]

comparison(arr1 , arr2)