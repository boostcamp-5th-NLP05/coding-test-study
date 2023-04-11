N, M = map(int,input().split())
data = []
for i in range(N):
    data.append(int(input()))

data.sort()
d = [100000] * (M+1) #d는 i를 만들기 위해 필요한 화폐 개수
if data[0] <= M and data[1] <= M: #만들고자 하는 화폐가 가지고있는 화폐보다 작을경우 -1반환을 위해 추가한 조건문
    d[data[0]] = 1 #가지고 있는 화폐 중 가장 작은 화폐 만들 수 있는 경우의 수 1
    d[data[1]] = 1 #가지고 있는 화폐 중 두번째로 작은 화폐 만들 수 있는 경우의 수 1

for i in range(3, M+1):
    for j in data: #화폐 하나하나씩 넣어가며 최소를 구함
        if i - j >= 0 and i - j <= M:
            d[i] = min(d[i - j]+1,d[i])

if d[M] == 100000: #화폐 만들기 불가능한 경우
    print(-1)
else:
    print(d[M])