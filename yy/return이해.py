
def m(x):
    if x == 0:
        return x

    else:
        y = m(x-1)
        print(x)
        print(y)

m(3)