N = int(input())
data = dict()
for i in range(N):
    name, score = list(input().split())
    score = int(score)
    data[score] = name #점수를 key, 이름을 name으로 힌 dictionary생성
sorted_data = sorted(data.items(), key = lambda item: item[0]) # key로 정렬 / key = data.keys()는 key만 뽑아서 안되네요..
for d in sorted_data: #튜플형식으로 반환되어 1번째인 value만 출력
    print(d[1], end = ' ')