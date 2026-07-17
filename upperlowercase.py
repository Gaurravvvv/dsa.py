str=input()
uppercnt=0
lowercnt=0
for i in range(len(str)):
    if str[i].isupper():
        uppercnt+=1
    else:
        lowercnt+=1

if uppercnt > lowercnt:
    print(str.upper())
else:
    print(str.lower())   

    