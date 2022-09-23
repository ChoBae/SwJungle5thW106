n = int(input())
c = []
for i in range(n):
    ai,bi = map(int, input().split())
    c.append(ai+bi)
    
for d in c:
    print(d)