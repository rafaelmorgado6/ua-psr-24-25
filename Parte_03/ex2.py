def addComplex(x,y):
    
    real = x[0] + y[0]
    im = x[1] + y[1]
    result = (real, im)
    
    return (real, im)


def multiplyComplex(x,y):
    
    result = (x[0]*y[0] -  x[1]*y[1], x[0]*y[1] + x[1]*y[0])
    
    return result

def printComplex(x):
    
    print(f"{x[0]} + {x[1]}i")


def main():
    c1 = (5, 3)
    c2 = (-2, 7)
    
    c = addComplex(c1,c2)
    printComplex(c)
    printComplex(multiplyComplex(c1,c2))

if __name__ == "__main__":
    main()