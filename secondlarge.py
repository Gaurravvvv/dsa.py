def secondlarge(arr):
    large = arr[0]
    slarge = arr[1]
    temp = slarge

    if len(arr)==0:
        return None
    if len(arr)<2:
        return arr[0]
    
    
    for i in arr:
        if large>=i and slarge!=i and slarge<i:
            slarge = i
        if i<=large and i>=temp:
            slarge = temp
        if large<i:
            slarge = large
            large = i

    print(large , slarge)

    return (slarge-1)*(large-1)

print(secondlarge([9,8,7]))
