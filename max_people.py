def max_people(hr , entry , exit):
    maxi = 0
    rem = 0
    for i in range(hr):

        maxi = max((rem+entry[i]) - exit[i] , maxi)
        rem = rem+entry[i]-exit[i]

    return maxi


hr = 6

entry = [3 , 2 , 4 , 0 , 1 , 2]
exit = [ 0 , 1 , 3 , 2 , 2 , 1]

print("Max Guests : " , max_people(hr , entry , exit))
