n = int(input())

n_list = []
n_list = map(int, input().split())
r_count = 0

for i in n_list:
    count = 0
    for j in range(2, i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        r_count +=1
        
print(r_count)