n,x = map(int, input().split())
a = list(map(int, input().split()))

b = []
for i in a:
    if i < x:
        b.append(i)
        
for d in b:
    print(d, end=' ')