# 곱셈 2588
firstNum = input()
secNum = input()

for i in reversed(secNum):
    tmp = 0
    tmp += int(firstNum) * int(i)
    print(tmp)
print(eval(firstNum+"*"+secNum))