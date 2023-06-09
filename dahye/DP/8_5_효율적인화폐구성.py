N, M = map(int,input().split())
data = []
for i in range(N):
    data.append(int(input()))

data.sort()
d = [100000] * (M+1) #d는 i를 만들기 위해 필요한 화폐 개수

for j in data:
    if j <= M : #만들고자 하는 화폐가 가지고있는 화폐보다 작을경우 -1반환을 위해 추가한 조건문
        d[j] = 1 #가지고 있는 화폐 경우의 수 1

for i in range(3, M+1):
    for j in data: #화폐 하나하나씩 넣어가며 최소를 구함
        if i - j >= 0 :
            d[i] = min(d[i - j]+1,d[i])

if d[M] == 100000: #화폐 만들기 불가능한 경우
    print(-1)
else:
    print(d[M])