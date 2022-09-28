## 2667 단지번호 붙히기
# from collections import deque

## bfs 풀이
# n = int(input())
# maps = [list(input()) for _ in range(n)]
# visited = [[False] * n for _ in range(n)]
# # 상하좌우
# dx = [1, -1, 0, 0]
# dy = [0, 0, -1, 1]
# res = []

# def bfs(i, j):
#     q = deque([(i, j)])
#     cnt = 1
#     while q:

#         x, y = q.popleft()
#         visited[x][y] = True

#         for z in range(4):
#             nx = x + dx[z]
#             ny = y + dy[z]
#             if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] == '1' and not visited[nx][ny]:
#                 q.append([nx,ny])
#                 maps[nx][ny] = '0'
#                 # print(nx,ny)
#                 cnt += 1

#     return cnt
# for i in range(n):
#     for j in range(n):
#         if maps[i][j] == '1' and not visited[i][j]:
#             res.append(bfs(i, j))


# print(len(res))
# res.sort()
# for r in res:
#     print(r)



## dfs 풀이
n = int(input())
maps = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
res = []


def dfs(x, y):
    global cnt
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] == '1' and not visited[nx][ny]:
            maps[nx][ny] = '0'
            cnt += 1
            dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if maps[i][j] == '1' and not visited[i][j]:
            cnt = 1
            dfs(i, j)
            res.append(cnt)


print(len(res))
res.sort()
for r in res:
    print(r)
