def decode(s):
    # sc="1234567890-=WERTYUIOP[]\SDFGHJKL;'XCVBNM,./"
    sc="1234567890QWERTYUIOPASDFGHJKLZXCVBNM,./;'[]\-=`"
    for i in s:
        if i in sc :
            j=0
            while i!=sc[j]:
                j+=1
            print(sc[j-1],end="")
        else:
            print(i,end="")

decode("O S, GOMR YPFSU/")

