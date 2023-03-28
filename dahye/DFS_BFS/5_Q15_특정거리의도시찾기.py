from collections import deque

n, m, k, x= map(int, input().split())
data = []
for _ in range(m):
    data.append(list(map(int, input().split())))

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
            if temp == check[0]:
                other = check[1]
            elif temp == check[1]:
                other = check[0]
            else:
                continue

            if temp in check and visited[other] == -1: #처음 방문여부
                queue.append(other) #temp update
                visited[other] = visited[temp] + 1 #원래 temp가 인덱스였던 visited 값에 1추가
            if visited[temp] == k: # 구하는 거리 k면 
                answer.append(temp) #저장
            if visited[temp] > k: #k를 넘어가면
                break #탈출
                

    if len(answer) == 0:
        return -1
    return answer

print(bfs(x))