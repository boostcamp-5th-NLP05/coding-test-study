N = int(input())
data = list(map(int,input().split()))


d = [1] * N # 0번부터 i번째 병사중 참여할 수 있는 최대 병사 수
for i in range(1, N):
    for j in range(i):
        if data[i] < data[j] : #앞에 전투력이 큰 병사가 있을 때
            d[i] = max(d[i],d[j]+1) #참여, 어느 i번째 뒤에 참여할지를 max로 업데이트

print(N-max(d)) #전체에서 최대병사 수 빼서 열외 병사 수 구함