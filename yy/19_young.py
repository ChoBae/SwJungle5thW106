a,b = input().split()

revers_a = int(a[::-1])
revers_b = int(b[::-1])

if revers_a > revers_b:
    print(revers_a)
else:
     print(revers_b)