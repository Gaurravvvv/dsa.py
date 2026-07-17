def codevita(p1 , p2 , p3 , q , r , e):
    part = e-r
    two = (p1-q)+(p2-q)+(p3-q)
    one = part - two - q

    first = (one/3)+(p1+p3-q)
    return one , first

# p1 = int(input("Enter P1 : "))
# p2 = int(input("Enter P2 : "))
# p3 = int(input("Enter P3 : "))
# q = int(input("Enter q : "))
# e = int(input("Enter e : "))
# r = int(input("Enter r : "))

p1 = 30
p2 = 26
p3 = 28
q = 14
e = 345
r = 43

print(codevita(p1 , p2 , p3 , q , r , e))
