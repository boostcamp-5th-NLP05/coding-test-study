from collections import deque
import copy

#노드의 개수와 간선의 개수를 입력 받기
N = int(input())

#모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (N+1)
#각 강의의 강의 시간 저장
course = [0] * (N+1)

#각 노드에 연결된 간선 정보를 담기 위한 연결 리스트를 초기화
graph=[[] for i in range(N+1)]

#방향 그래프의 모든 간선 정보를 입력 받기
for n in range(1, N+1):
    temp = list(map(int,input().split()))
    course[n] = temp[0]
    for t in temp[1:-2]:
        graph[t].append(n) # graph[t]는 t번째 강의를 듣기위해 선이수를 해야하는 강의들
        indegree[n] += 1 #진입 차수를 1 증가

#위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(course) #강의 시간을 담고 최대로 업데이트하는 방식
    q = deque() #큐 기능을 위한 deque 라이브러리 사용

    #처음시작할 때는 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1,N+1):
        if indegree[i] == 0:
            q.append(i)

    #큐가 빌 때까지 반복
    while q:
        #큐에서 원소 꺼내기
        now = q.popleft()
        #해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            result[i] = max(result[i], result[now] + course[i])
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
        #위상 정렬을 수행한 결과 출력
    for i in result[1:]:
        print(i)

topology_sort()