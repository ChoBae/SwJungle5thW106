def hancheck(n):
    count = 0
    for i in range(1, n+1):
        numlist = list(map(int,str(i)))
        if i < 100:
            count += 1
        elif numlist[0]-numlist[1] == numlist[1]-numlist[2]:
            count += 1
    return count

a = int(input())
print(hancheck(a))
