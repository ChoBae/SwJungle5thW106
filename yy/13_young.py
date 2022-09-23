n =int(input())

a = []
for i in range(n):
    num_list = list(map(int, input().split()))
    count = 0
    ave = sum(num_list[1:])/num_list[0]
    for j in num_list[1:]:
        if j > ave:
            count += 1
    rate = count/num_list[0] * 100 
    a.append(rate)
    
for k in range(n):
    print(f'{a[k]:.3f}%')