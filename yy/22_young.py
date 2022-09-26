def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i ==0:
            return False
    return True


t = int(input())
resert_1= []
resert_2= []

for _ in range(t):
    r = int(input())
    a, b = r//2, r//2
    while True:
        if is_prime(a) and is_prime(b):
            # resert_1.append(a)
            print(a, b)
            # resert_2.append(b)
            break
        else:
            a -= 1
            b += 1
# for j in range(t):
#     print(resert_1[j], resert_2[j])