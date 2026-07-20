def outer():
    #global a
    a = 20

    def inner():
        #global a
        a = 30
        print(a)

    inner()
    print(a)

a = 10
outer()
print(a)