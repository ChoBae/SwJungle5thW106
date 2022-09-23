# 사칙연산 브5
oper = ['+', '-', '*', '/', '%']
a,b = map(str, input().split())
for i in range(5):
    print(int(eval(a+oper[i]+b)))
