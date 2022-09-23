a,b,c,d = map(int, input().split())

ca = c-a
db = d-b
a0 = a-0
b0 = b-0

if ca < db and ca < a0 and ca < b0:
    print(ca)
elif db < ca and db < a0 and db < b0:
    print(db)
elif a0 < ca and a0 < db and a0 < b0:
    print(a0)
else:
    print(b0)