# 2869 달팽이는 올라가고 싶다
A, B, V = map(int, input().split())
day = (V - B)/(A - B)

print(int(day) if day == int(day) else int(day) + 1)
