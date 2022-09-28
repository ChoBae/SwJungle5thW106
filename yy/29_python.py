# 재귀함수 N QUEEN 9663
def cornfirm(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True

def n_queen(x):
    global result
    
    if x ==n:
        result +=1
    else:
        for i in range(n):
            row[x] = i
            if cornfirm(x):
                n_queen(x+1)


result = 0

n = int(input())
row = [0] * n
n_queen(0)
print(result)