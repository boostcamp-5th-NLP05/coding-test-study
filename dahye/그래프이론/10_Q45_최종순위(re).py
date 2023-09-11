from collections import deque
import sys

def input():
    return sys.stdin.readline().rstrip()
#위상 정렬 함수
def topology_sort(n, data):
    #모든 노드에 대한 진입차수는 0으로 초기화
    indegree = [0] * (n)

    #각 노드에 연결된 간선 정보를 담기 위한 연결 리스트를 초기화
    graph=[[] for _ in range(n)]

    #방향 그래프의 모든 간선 정보를 입력 받기
    for i in range(n-1):
        for j in range(i+1,n):
            graph[data[j]-1].append(data[i]-1)
            #진입 차수를 1 증가
            indegree[data[i]-1] += 1

    m = int(input())
    for _ in range(m):
        a,b = map(int,input().split()) # 순위를 바꿀 팀 입력
        a = a-1
        b = b-1 #index 0부터 시작하도록 설정하여 맞춰줌
        if b in graph[a]: # b가 더 높은 순위였다면
            graph[b].append(a)
            graph[a].remove(b)
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[a].append(b)
            graph[b].remove(a)
            indegree[a] -= 1
            indegree[b] += 1


    result = [] #알고리즘 수행 결과를 담을 리스트
    q = deque() #큐 기능을 위한 deque 라이브러리 사용

    #처음시작할 때는 진입 차수가 0인 노드를 큐에 삽입
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    #큐가 빌 때까지 반복
    while q:
        #큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now+1) #결과리스트에 해당 노드 순서대로 삽입
        #해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    if len(result) == n:
        print(list(reversed(result)))
    else:
        print("IMPOSSIBLE")


t = int(input())
for _ in range(t):
    n = int(input())
    data = list(map(int,input().split()))
    topology_sort(n, data)