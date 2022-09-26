# 완전탐색 일곱 난쟁이 2309

m = [int(input()) for _ in range(9)]
m_sum = sum(m)

for i in range(9):
    for j in range(i+1, 9):
        if m_sum - (m[i] + m[j]) == 100:
            a = m[i]
            b = m[j]
            # m.remove(m[i])
            # m.remove(m[j])
m.remove(a)
m.remove(b)
m.sort()
for k in m:
    print(k)
