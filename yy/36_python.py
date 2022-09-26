# 완전탐색 블랙잭 2798

n , m = map(int, input().split())

a= list(map(int, input().split()))
select_card = []

for i in range(n):
    for j in range(1+i, n):
        for k in range(j+1, n):
            if a[i] + a[j] + a[k] <= m:
                select_card.append((a[i] + a[j] + a[k], a[i], a[j], a[k]))

select_card.sort(reverse=True)
print(select_card[0][0])
