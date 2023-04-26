import heapq
inf = int(1e9)


m = int(input())

move = [(1,0),(-1,0),(0,1),(0,-1)] 
answer = []

for _ in range(m):
    n = int(input())
    
    distance = [[inf] * (n) for _ in range(n)] #거리 테이블 2차원으로 초기화
    
    graph = []
    for _ in range(n):
        graph.append(list(map(int,input().split())))
        
    q = []
    distance[0][0] = graph[0][0] #거리 테이블 (0,0) 값 채우기
    heapq.heappush(q,[distance[0][0],[0,0]])
    
    while q: #다익스트라 알고리즘
        dist, now = heapq.heappop(q)
        row, col = now
        if distance[row][col] < dist:
            continue
        
        for r,c in move: #네 방향에 있는 값들이 이동 비용
            if (row+r) in [-1,n] or (col+c) in [-1,n]:
                continue
            
            cost = dist + graph[row+r][col+c]
            
            if cost < distance[row + r][col + c]:
                distance[row + r][col + c] = cost
                heapq.heappush(q,[cost,[row+r,col+c]])  

    answer.append(distance[n-1][n-1])


for i in range(m):
    print(answer[i])