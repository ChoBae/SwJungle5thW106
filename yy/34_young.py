# 단어 정렬 1181

n = int(input())
a = [input() for _ in range(n)]
a = list(set(a))
a_tu = []

for i in a:
    a_tu.append((len(i), i))

resert = sorted(a_tu)

for len_w , w in resert:
    print(w)

## 풀이2 람다식 