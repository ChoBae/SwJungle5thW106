# 평균은 넘겠지
c = int(input())
ResLi = []
for _ in range(c):
    n = list(map(int, input().split()))

    GradeList = n[1:]
    Average = sum(GradeList) / len(GradeList)
    Cnt = 0
    for i in GradeList:
        if i > Average:
            Cnt += 1

    res = Cnt/len(GradeList) * 100
    resView = f'{res: .3f}'
    print(resView[1:] + "%")

