a = int(input())
b = input()

mul_1 = a*int(b[2])
mul_2 = a*int(b[1])
mul_3 = a*int(b[0])

mul_add = mul_1 + mul_2*10 + mul_3*100

print(mul_1)
print(mul_2)
print(mul_3)
print(mul_add)