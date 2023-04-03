N = int(input())
data = []
for i in range(N):
    data.append(int(input()))

data.sort(reverse=True) #내림차순으로 정렬
for d in data:
    print(d, end = ' ')