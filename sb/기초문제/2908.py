# 상수
a, b = map(str, input().split())
RevA = int(a[::-1])
RevB = int(b[::-1])
print(RevA if RevA > RevB else RevB)