import math
def f(x):
    return x**3

def g(x):
    return math.exp(x)

if __name__ == '__main__':

    x = 1.7
    delta = 0.01
    area = 0

    while(x >= 1.7 and x <= 4.6):
        fx = 0.00
        gx = 0.00
        fx += f(x) 
        gx += g(x) 
        x += delta 
        if fx > gx:
            area += abs(fx - gx) * delta
            #print(area, x)
    print(round(area,3))
