import sys
import copy

def shark_move(before_map, shark_dir): #상어를 이동하면서 냄새 업데이트
    d = [(1,0),(0,-1),(0,1),(-1,0)]
    current_map = copy.deepcopy(before_map)
    current_dir = copy.deepcopy(shark_dir)
    for i in range(N):
        for j in range(N):
            # 냄새가 남아있는 경우 (1이면 사라지므로 1초과)
            if current_map[i][j][1] > 1:
                current_map[i][j][1] -= 1
            # 상어가 존재하는 위치의 경우
            if current_map[i][j][0] != 0:
                move = True
                while move:
                    temp_dir = shark_dir[current_map[i][j][0]-1] % 4 #상어 이동방향
                    ni = i + d[temp_dir][0]
                    nj = j + d[temp_dir][1]
                    if 0 <= ni < N and 0 <= nj < N:
                        if current_map[ni][nj][1] == 0: # 냄새가 나지 않는 곳이라면
                            # 상어 이동시키기
                            if current_map[ni][nj] == 0:
                                
                                move = False # 이동완료




    return current_map, current_dir


def input():
    return sys.stdin.readline().rstrip()

N,M,k = map(int, input().split())
before_map = []
shark_loc = []
for _ in range(N):
    before_map.append(list(map(int, input().split())))
#list로 칸의 상어냄새, 냄새가 사라지기까지 남은시간 저장

shark_dir = list(map(int, input().split())) #상어의 방향 shark_dir[0]은 1번상어의 방향
# for i in range(N):
#     for j in range(N):
#         if before_map[i][j] != 0:
#             dd

shark_info = [] # 우선순위 정보
for i in range(M):
    temp = []
    for _ in range(4):
        temp.append(list(map(int, input().split())))
    shark_info.append(temp)


time = 0
while True:


    if time >= 1000:
        print(-1)
        break