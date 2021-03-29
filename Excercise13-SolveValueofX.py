def f(x):
    value = (x**5)-(x**4)+2*(x**3)-(x**2)+x
    return value


if(__name__ == "__main__"):
    x_l = 1.00000
    x_u = 1.50000
    x = (x_l + x_u)/2

    while(f(x) > 3.00000):
        x = (x_l + x_u)/2.00000

        if(f(x)<3):
            x_l = x
        else:
            x_u = x

    #print("x is between " + str(x_l) + " and " + str(x_u) ) #+ " and f(x) is " + str(f(x)) )

    while(f(x) < 3.00000 ):
        x_l = x_l + 0.00001
        if(x_l >= x_u):
            break
        else:
            x = round(x_l, 5)
    x = x - 0.00001
    print(round(x,5))
        
