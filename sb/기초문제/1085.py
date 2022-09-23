# 직사각형에서 탈출
x, y, w, h = map(int, input().split())
hei = w - x 
wid = h - y
print(min(x,y, hei, wid))