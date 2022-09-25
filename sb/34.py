# 1181 단어 정렬
n = int(input())    # 입력
WordList = [ input() for _ in range(n)] # 리스트 컴프리헨션
WordList.sort() # 1. 단어리스트 오름차순정렬   
WordList.sort(key=lambda x: len(x)) # 2. 단어리스트 람다식으로 단어의 길이를 기준으로 오름차순 정렬
print(WordList) # 출력
    