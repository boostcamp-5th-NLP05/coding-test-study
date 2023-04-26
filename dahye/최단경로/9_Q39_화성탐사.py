import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

T = int(input()) #test case 수

def detect(n, data): #최소 비용을 구하는 함수 -> 다익스트라 이용
    graph = [[] for _ in range(n*n+1)] # 각 좌표를 1차원으로 생각하여 비용 추가
    distance = [INF] * (n*n+1)

    for i in range(n):
        for j in range(n):
            temp1 = n*i+j+1-1 #좌
            temp2 = n*i+j+1+1 #우
            temp3 = n*(i+1)+j+1 #하
            temp4 = n*(i-1)+j+1 #상
            if temp1 > n*(i-1) + (n-1) +1 : # 가장 왼쪽 기계는 더이상 왼쪽으로 이동할 수 없음
                graph[n*i+j+1].append((temp1,data[i][j]))
            if temp2 < n*(i+1)+1 : # 가장 오른쪽 기계는 더이상 오른쪽으로 이동할 수 없음(오른쪽 이동에서 다음 idx가 밑으로 내려가지 않도록 조건 설정)
                graph[n*i+j+1].append((temp2,data[i][j]))
            if temp3 < n*n+1 : 
                graph[n*i+j+1].append((temp3,data[i][j]))
            if temp4 > 0 : 
                graph[n*i+j+1].append((temp4,data[i][j]))
                    
    q = []
    heapq.heappush(q, (0,1))
    distance[1] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
			# 현재 노드를 거쳐서 다른 노드로 이동하는 비용이 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance[-1] + graph[-1][-1][-1] # 다음노드에 이동하면서 얻는 비용으로 계산했으므로 맨 마지막 이동까지 고려해주어야한다.


ans = []
# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(T):
    n = int(input())
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))
    ans.append(detect(n, data))

for t in range(T):
    print(ans[t])