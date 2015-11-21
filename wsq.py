# wsq14

def calculateE(n):
    c = 1
    s = 1
    x = 1
    while True:
        s += x*(1/c)
        x = (1/c)*x
        number = s + x*(1/c)
        if (number - s) < n:
            break
        c += 1
    return s

a= float(input("Give me a number to calculate: "))
print (calculateE(a))
