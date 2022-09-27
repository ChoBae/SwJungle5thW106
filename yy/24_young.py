# 수학 종이자르기 2628

x, y = map(int, input().split())
n = int(input())

garo = [int(0)]
sero = [int(0)]

for _ in range(n):
    a, b = map(int, input().split())
    if a == 0:
        garo.append(b)
    else:
        sero.append(b)

garo.append(y)
sero.append(x)
garo.sort()
sero.sort()

max_garo = 0
max_sero = 0
for i in range(1, len(garo)):
    gap = garo[i] - garo[i-1]
    if gap > max_garo:
        max_garo = gap

for j in range(1, len(sero)):
    gap = sero[j] - sero[j-1]
    if gap > max_sero:
        max_sero = gap

print(max_garo * max_sero)