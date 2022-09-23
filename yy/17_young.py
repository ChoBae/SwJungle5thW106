n = int(input())

resert = []
for _ in range(n):
    a,b = input().split()
    m_resert =""
    for i in b:
        mul = i*int(a)
        m_resert += mul
    resert.append(m_resert)

for j in range(n):
    print(resert[j])
    