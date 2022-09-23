# # 2557
# print("Hello World!")


# #10869
# a, b = map(int, input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)


# # 2588
# A = int(input())
# B = input()

# # 문자열의 인덱스를 이용해서 두번째 입력 받은 문자를 하나씩 숫자로 반환하고 A와 곱한다.
# AxB2 = A * int(B[2])
# AxB1 = A * int(B[1])
# AxB0 = A * int(B[0])
# AxB = A * int(B)

# print(AxB2, AxB1, AxB0, AxB, sep='\n')


# #9498
# a = int(input())

# if 90<= a and a <= 100:
#     print("A")
# elif 80<= a and a <= 89:
#     print("B")
# elif 70<=a and a<=79:
#     print("C")
# elif 60<=a and a<=69:
#     print("D")
# else:
#     print("F")


# # 2753
# year =  int(input())

# if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
#     print(1)
# else:
#     print(0)


# #1085
# x, y, w, h = map(int, input().split())
# ary = []
# ary.append(x)
# ary.append(w-x)
# ary.append(y)
# ary.append(h-y)

# print(sorted(ary)[0])


# #2739
# a = int(input())

# for i in range(1, 10):
#     print(f"{a} * {i} = {a*i}")


# #10950
# T = int(input())
# for i in range(T):
#     A, B = map(int, input().split())
#     print(A+B)


# #2438
# n = int(input())

# for i in range(1, n+1):
#     print("*"*i)


# #10871
# N, X = map(int, input().split())
# tmp = list(map(int, input().split()))
# for a in tmp:
#     if a < X:
#         print(a, end=" ")


# #2562
# tmp = 0
# idx = 0
# for i in range(1, 10):
#     a = int(input())
#     if tmp < a:
#         tmp = a
#         idx = i

# print(tmp)
# print(idx)


# #8958
# T = int(input())
# for _ in range(T):
#     tmp = input()
#     p = 0
#     ans = 0
#     for a in tmp:
#         if a == 'O':
#             p += 1
#         else:
#             p = 0
#         ans += p

#     print(ans)


# #4344
# #round함수는 끝의 0을 생략해버린다.
# for _ in range(int(input())):
#     ary = list(map(int,input().split()))
#     N = ary[0]
#     cnt = 0
#     for i in range(1, len(ary)):
#         if ary[i] > (sum(ary)-N)/N:
#             cnt += 1
#     print(f"{cnt/N*100:.3f}%")


# #2577
#딕셔너리 이용 풀이
# A = int(input())
# B = int(input())
# C = int(input())
# a = str(A*B*C)

# data = dict()
# for i in range(0, 10):
#     data[str(i)] = 0

# for num in a:
#     data[num] += 1

# for val in list(data.values()):
#     print(val)

# #일반 배열 이용 풀이
# a=int(input())
# b=int(input())
# c=int(input())

# idx = list()
# for i in range(0,10):
# 	idx.append(0)
# res = str(a*b*c)
# for i in range(0, len(res)):
# 	idx[int(res[i])] += 1
# for i in range(0, len(idx)):
# 	print(idx[i])

# #count 내장함수 사용 풀이
# a = int(input())
# b = int(input())
# c = int(input())
# tmp = a * b * c
# for i in range(9):
#     print(str(tmp).count(str(i)))


# #15596
# ans = sum(a)


# #11654
# asc = input()
# print(ord(asc))


#2675
# 배열 쓰는 방법
# T = int(input())
# for _ in range(T):
#     R, S = map(str, input().split())
#     res = []
#     for s in S:
#         print(s*int(R), end='')
#         for _ in range(int(R)):
#             res.append(s)
#     print(''.join(res))

# # 배열 따로 안쓰고 바로 출력하는 방법
# n = int(input())

# for _ in range(n):
#     cnt, word = input().split()
#     for x in word:
#         print(x*int(cnt), end='')
#     print()


# #1152
# a = list(input().split())
# print(len(a))


# #2908
# a, b = input().split()
# if a[::-1] > b[::-1]:
#     print(a[::-1])
# else:
#     print(b[::-1])


# #2869
# #1번 풀이
# #마지막으로 올라가기 전날 까지 세고,
# #올라갔다가 도착하면 print.
# #내용은 같은데 2번 방법이 더 깔끔함.
# import math
# A, B, V = map(int, input().split())
# tmp = (V-A)%(A-B)
# while True:
#     tmp = tmp - A
#     if tmp <= 0:
#         print(math.ceil((V-A)/(A-B)) + 1)
#         break
#     tmp = tmp + B

# # #2번 풀이
# # #
# # import math
# # A, B, V = map(int, input().split())
# # day = (V - B) / (A - B)
# # print(math.ceil(day))


#1978
T = int(input())
ary = list(map(int, input().split()))
#소수: 약수로 1과 자기 자신만을 갖는 수.

res = 0
for num in ary:
    idx = 1
    count = 0
    while idx <= num:
        if num % idx == 0:
            count += 1
        idx += 1
    if count == 2:
        res += 1
print(res)
