def coordinates(arr , key):
    row = len(arr)
    col = len(arr[0])
    for i in range(row):
        for j in range(col):
            if arr[i][j]==key:
                return f"({i} , {j})"


arr = [[1 , 2 , 3] , [4 , 5 , 6] , [7 , 8 , 9]]
key = 3
print(coordinates(arr , key))