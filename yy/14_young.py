a = int(input())
b = int(input())
c = int(input())

mul = a*b*c
mul_str = str(mul)

for i in range(10):
    print(mul_str.count(str(i)))
    