def freq(str , ch):

    dict = {}
    for i in str:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1

    return dict[ch]


def freqq(str , ch):
    cnt = 0 
    for i in str:
        if i == ch:
            cnt+=1
    

    return cnt

    



str = input("Enter Str : ")
ch = input("Enter Character : ")

print(freq(str , ch))
print("Cnt Method" , freqq(str , ch))