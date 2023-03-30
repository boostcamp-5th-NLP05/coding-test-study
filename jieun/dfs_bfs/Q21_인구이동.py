# 백준 16234 정답: 34200 KB, 5532 ms, Python3
import sys
from collections import deque

N,L,R = map(int, sys.stdin.readline().rstrip().split())
map_ = []
for _ in range(N):
    map_.append(list(map(int, sys.stdin.readline().rstrip().split())))

step = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(sr, sc, visited):
    # 나라 (sr,sc)가 속한 연합을 구하고 인구 이동
    # 인구 이동을 할 수 없으면 False 반환
    
    group = [(sr, sc)] # 큐 대신 사용. 연합 속 나라 저장
    visited[sr][sc] = True
    
    idx = 0
    while idx < len(group):
        r, c = group[idx]
        for dr, dc in step:
            nr = r + dr
            nc = c + dc
            if nr in [-1, N] or nc in [-1, N] or visited[nr][nc]: continue
            
            # 인구 차이 확인
            diff = abs(map_[r][c] - map_[nr][nc])
            if diff < L or diff > R: continue
            
            visited[nr][nc] = True
            group.append((nr, nc))
        idx += 1
    
    # 국경선 연 나라가 없어서 인구 이동 안 함
    if len(group) == 1: return False
    
    sum = 0
    for r,c in group: sum += map_[r][c]

    # 연합 나라의 인구 변경
    people = int(sum/len(group))
    for r,c in group: map_[r][c] = people
    
    return True
        

day = 0
while True:
    visited = [[False for _ in range(N)] for _ in range(N)]

    move = False # 인구 이동한 연합이 하나라도 있으면 True.
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                move = move | bfs(r, c, visited)
                
    # 인구 이동한 연합이 없으므로 break
    if not move: break 
    
    day += 1

print(day)
