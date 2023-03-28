from collections import deque

n, m, k, x= map(int, input().split())
data = []
for _ in range(m):
    data.append(list(map(int, input().split())))

#인접리스트로 변환하면서 받기
# data = [[] for _ in range(n+1)]
# for _ in range(m):
#     d1, d2 = map(int, input().split())
#     data[d1].append(d2)

#code
#dfs - 깊이로 탐색하여 최단거리가 k가 맞는지 하나하나 확인
#라고 생각했으나 모든 거리가 1이라 bfs라 한다....

def bfs(x) :
    answer = []
    visited = [-1 for _ in range(n+1)]
    queue = deque().append((x))
    visited[x] = 0 #타겟의 거리를 0으로 설정
    while queue:
        temp = queue.popleft()
        for check in data:
            # elif temp == check[1]: 단방향이므로 삭제
            #     other = check[0]
            other = check[1]
            if temp in check and visited[other] == -1: #처음 방문여부
                queue.append(other) #temp update
                visited[other] = visited[temp] + 1 #원래 temp가 인덱스였던 visited 값에 1추가
            if visited[other] == k: # 구하는 거리 k면 
                answer.append(other) #저장
    if len(answer) == 0:
        return -1
    return answer

print(bfs(x))