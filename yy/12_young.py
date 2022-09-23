n = int(input())

a =[]
for i in range(n):
    ox_list = input()
    score = 0
    sum_score = 0
    for j in ox_list:
        if j == "O":
            score += 1
            sum_score += score
        else:
            score = 0
    a.append(sum_score)

for k in range(n):
    print(a[k])