from collections import deque

n = int(input())
indegree = [0] * (n+1)
graph = [[] for i in range(n+1)]
time = [0] * (n+1)

for i in range(1,n+1):
    tmp = list(map(int, input().split()))
    time [i] = tmp[0]
    for j in tmp[1:-1]:
        indegree[i] += 1
        graph[j].append(i)

    
def topology_sort():
    result = time.copy()
    q = deque()
    
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
            
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
                
    for i in result[1:]:
        print(i)
        
topology_sort()