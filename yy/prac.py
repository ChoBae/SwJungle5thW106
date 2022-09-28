def prac(n):
    if n == 1:
        print(n)
        n += 1
        return
    else: 
        # print(n)
        prac(n-1)
        print(n)
prac(5)
