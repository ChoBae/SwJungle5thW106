# 최댓값
NumList = []
for _ in range(9):
    NumList.append(int(input()))

# 최댓값
MaxNum = max(NumList)
print(MaxNum)
print(NumList.index(MaxNum)+1)
