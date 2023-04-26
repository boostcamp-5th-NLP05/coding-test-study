import heapq
INF = int(1e9)

steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def solve():
    N = int(input())
    map_ = []
    for _ in range(N):
        map_.append(list(map(int, input().split())))
    cost = [[INF for _ in range(N)] for _ in range(N)]
    
    q = []
    heapq.heappush(q, (map_[0][0],0,0)) # cost, r, c
    cost[0][0] = map_[0][0]
    
    while q:
        ccost, r, c = heapq.heappop(q)
        if ccost > cost[r][c]: continue
        for dr, dc in steps:
            nr = r + dr
            nc = c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
            ncost = ccost + map_[nr][nc]
            if ncost < cost[nr][nc]:
                cost[nr][nc] = ncost
                heapq.heappush(q, (ncost, nr, nc))
    
    print(cost[N-1][N-1])
    
    

T = int(input())

while T:
    T -= 1
    solve() # 각 테스트케이스 처리   