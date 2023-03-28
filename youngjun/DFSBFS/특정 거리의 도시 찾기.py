#98848KB	1560ms
from collections import deque
import sys

n, m, k, x= map(int,sys.stdin.readline().rstrip().split())

data = [[] for _ in range(n+1)]

for _ in range(m):#인접 리스트 생성
    start, end = map(int, sys.stdin.readline().rstrip().split())
    data[start].append(end)

queue = deque()
queue.append((x,0)) #처음 도시와 cnt = 0 으로 큐에 넣어줌
visited = [False] * (n+1) #방문 표시
answer = []


while queue:
    start,cnt = queue.popleft()

    if not visited[start]: #방문하지 않았을 때만 돌림

        visited[start] = True #방문 처리
        
        if cnt == k: #거리가 됐다면 answer 리스트에 넣어주고 다음 반복
            answer.append(start) 
            continue

        for i in data[start]: #갈 수 있는 도시 큐에 추가
            queue.append((i,cnt+1))
                
answer.sort()

if len(answer) == 0:
    print(-1)
else:
    for i in answer:
        print(i)