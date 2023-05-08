# 통과 코드
import sys
from collections import deque
N = int(input())

dx = [-1,0,0,1] # 상 좌 우 하
dy = [0,-1,1,0]
room = []
sharksize = 2
sharkeat = 0

for i in range(N):
    room.append([int(x) for x in sys.stdin.readline().rstrip().split()])
    for j in range(len(room[i])):
        if room[i][j] == 9:
            room[i][j] = 0
            shark_x, shark_y = i, j

def finding_fish(sx,sy):
    global sharksize
    deq = deque()
    deq.append([sx,sy])

    visited = [[False for _ in range(N)] for _ in range(N)]
    distance = [[0 for _ in range(N)] for _ in range(N)]
    can_eat_fish = []

    while deq:
        x, y = deq.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if room[nx][ny] <= sharksize and not visited[nx][ny]: #이동이 가능하면
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    deq.append([nx,ny])

                    if room[nx][ny] < sharksize and room[nx][ny] != 0: #물고기가 있고 그걸 먹을 수 있다면
                        can_eat_fish.append([nx ,ny,distance[nx][ny]])

    can_eat_fish.sort(key= lambda x : (x[2],x[0],x[1])) # 정렬은 거리, x, y 오름차순으로
    return can_eat_fish

if __name__ == '__main__':
    ans = 0

    while True:
        fishlist = finding_fish(shark_x,shark_y)

        if len(fishlist) == 0: # 먹을 수 있는 물고기가 없다면
            print(ans)
            exit(0)

        shark_x, shark_y, move_time = fishlist[0]

        sharkeat += 1
        if sharksize == sharkeat: #먹은 물고기수와 사이즈가 같다면
            sharkeat = 0
            sharksize += 1

        room[shark_x][shark_y] = 0 # 물고기 먹은 자리는 빈칸으로 바꿈
        ans += move_time









# 내가 푼 풀이
# import sys
# from collections import deque
#
# N = int(input())
#
# map_ = [list(map(int, input().split())) for i in range(N)]
#
# print(map_)
#
# # 왼 오
# dr = [0, 0]
# dc = [-1, 1]
#
#
# def find_init(map_):
#
#     for r in range(N):
#         for c in range(N):
#             if map_[r][c] == 9:
#                 return (r, c)
#
#     return None
#
#
# s, e = find_init(map_)
#
# eat_cnt = 0
# my_size = 2
#
#
# def new_bfs(r, c):
#     depth = 1
#
#     global eat_cnt
#     global my_size
#
#     visited = [[False for c in range(N)] for r in range(N)]
#     visited[r][c] = True
#
#     while True:
#
#         # 수평선 위
#         for j in range(2):
#             for i in range(depth + 1):
#                 for k in range(i):
#                     nr = r
#                     nc = c + dc[j] * k
#                     if not visited[nr][nc]:
#                         visited[nr][nc] = True
#
#                         if map_[nr][nc] < my_size:
#                             eat_cnt += 1
#
#                             if eat_cnt == my_size:
#                                 eat_cnt = 0
#                                 my_size += 1
#                                 return nr, nc
#
#         # 수평선 (x축)
#         for j in range(2):
#             for i in range(2 * depth + 1):
#                 nr = r
#                 nc = c + dc[j] * i
#
#                 if not visited[nr][nc]:
#                     visited[nr][nc] = True
#
#                     if map_[nr][nc] < my_size:
#                         eat_cnt += 1
#
#                         if eat_cnt == my_size:
#                             eat_cnt = 0
#                             my_size += 1
#
#                             return nr, nc
#
#         # 수평선 아래
#         for j in range(2):
#             for i in range(depth + 1):
#                 nr = r
#                 nc = c + nc[j] * i
#
#                 if not visited[nr][nc]:
#                     visited[nr][nc] = True
#
#                     if map_[nr][nc] < my_size:
#                         eat_cnt += 1
#
#                         if eat_cnt == my_size:
#                             eat_cnt = 0
#                             my_size += 1
#
#                             return nr, nc
#
#         depth += 1
#
#
#     if depth >= N :
#         return None
#
#
#
#
# # 맵의 범위를 넘어가서도 아무도 없다면 -> 엄마 상어 -> 종료
# # 먹을 수 있는 물고기가 없다면 -> 종료
#
# # 이 부분을 어떻게 처리 ? -> BFS 와 size 를 연결하면 될거 같음. -> 근데?
# # 거리가 같으면서 가장 위쪽, 가장 왼쪽을 어떻게 처리하지 ? 수평선으로 내려가는 BFS 를 진행하면 될 듯.
#
#
# time = 0
# while True:
#
#     result = new_bfs(s, e)
#     if result == None:
#         print(time)
#         break
#     else:
#         time += 1
#
#
#
#
#



