#처음 자신의 위치에 냄새 뿌림
#이후 1초마다 상하좌우 인접한 칸 중 하나로 이동 후 자신의 냄새 뿌림
#냄새는 k번 이동하면 사라짐
#상어는 이동할 때 아무 냄새가 없는 칸의 방향으로 방향을 잡고 그런칸이 없다면 자신의 냄새가 있는 곳으로
#이동할 수 있는 칸이 여러곳일 때 각각의 상어는 우선순위가 있다.
#겹치면 번호 작은 놈이 살아남음
#1번만 남을 떄 까지

import sys

def input():
    return sys.stdin.readline().rstrip()

n, m, k = map(int,input().split()) #n : 격자크기, m: 상어 마리수, k = 냄새 남아있는 시간

shark_loc = {}
for i in range(n):
    tmp = list(map(int,input().split()))
    if tmp != [0 for _ in range(n)]:
        for j in range(len(tmp)):
            if tmp[j] != 0:
                shark_loc[tmp[j]] = [i,j]

shark_dir = list(map(int,input().split())) #1:위 2:아래 3:왼쪽 4:오른쪽
shark_dir.insert(0, 0)

pri_list = [[]]
for _ in range(m):
    tmp = []
    for _ in range(4):
        tmp.append(list(map(int,input().split())))
    pri_list.append(tmp)


###test1

#n, m, k = [4,2,6]    
#shark_loc = {1:[0,0], 2:[3,3]}
#shark_dir = [0, 4, 3]
#pri_list = [[], [[1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3]], [[1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3]]]

###test 2
#n, m, k = [5,4,4]
#shark_loc = {3: [0, 4], 2: [1, 1], 1: [2, 0], 4: [2, 4]}
#shark_dir = [0, 4, 4, 3, 1]
#pri_list = [[], [[2, 3, 1, 4], [4, 1, 2, 3], [3, 4, 2, 1], [4, 3, 1, 2]], [[2, 4, 3, 1], [2, 1, 3, 4], [3, 4, 1, 2], [4, 1, 2, 3]], [[4, 3, 2, 1], [1, 4, 3, 2], [1, 3, 2, 4], [3, 2, 1, 4]], [[3, 4, 1, 2], [3, 2, 4, 1], [1, 4, 2, 3], [1, 4, 2, 3]]]

###test 3
#n, m, k = [5,4,1]
#shark_loc = {3: [0, 4], 2: [1, 1], 1: [2, 0], 4: [2, 4]}
#shark_dir = [0, 4, 4, 3, 1]
#pri_list = [[], [[2, 3, 1, 4], [4, 1, 2, 3], [3, 4, 2, 1], [4, 3, 1, 2]], [[2, 4, 3, 1], [2, 1, 3, 4], [3, 4, 1, 2], [4, 1, 2, 3]], [[4, 3, 2, 1], [1, 4, 3, 2], [1, 3, 2, 4], [3, 2, 1, 4]], [[3, 4, 1, 2], [3, 2, 4, 1], [1, 4, 2, 3], [1, 4, 2, 3]]]

###test4
#n, m, k = [4,5,6]
#shark_loc = {3: [1, 1], 2: [2, 0], 1: [2, 2], 4: [3, 1], 5: [3, 3]}
#shark_dir = [0, 3, 4, 2, 1, 3]
#pri_list = [[], [[4, 1, 3, 2], [4, 2, 3, 1], [1, 2, 4, 3], [2, 3, 1, 4]], [[1, 3, 2, 4], [4, 1, 3, 2], [4, 3, 2, 1], [1, 4, 3, 2]], [[2, 3, 1, 4], [4, 3, 2, 1], [1, 4, 3, 2], [4, 2, 3, 1]], [[4, 3, 2, 1], [1, 4, 3, 2], [1, 3, 2, 4], [3, 2, 1, 4]], [[2, 3, 1, 4], [3, 2, 4, 1], [2, 3, 4, 1], [1, 2, 4, 3]]]

#print(shark_loc)
#print(shark_dir)
#print(pri_list)

map_ = [[[0,0] for _ in range(n)] for _ in range(n)]


for i in range(1,m+1):
    r,c = shark_loc[i]
    map_[r][c] = [i,k]

move = [(0,0),(-1,0),(1,0),(0,-1),(0,1)] #1:위 2:아래 3:왼쪽 4:오른쪽
shark_list = [i for i in range(1,m+1)]
shark_list_tmp = [i for i in range(1,m+1)]
cnt = 0

while True:
    cnt += 1
    
    if cnt > 1000:
        cnt = -1
        break
    
    move_loc = []
    move_loc_info = []
    
    for i in shark_list: #움직이기
        r,c = shark_loc[i]
        dir_ = shark_dir[i]
        
        #1)냄새 없는 칸 찾기
        is_nosmell = False
        for j in pri_list[i][dir_-1]: 
            ndir_ = j #우선순위 방향
            nr = r + move[ndir_][0]
            nc = c + move[ndir_][1]
            if nr in [-1,n] or nc in [-1,n]:
                continue
            if map_[nr][nc] == [0,0]:
                is_nosmell = True
                break

        if not is_nosmell: #2)냄새 없는 칸 없어서 자신 냄새 칸으로 갈 때
            for j in pri_list[i][dir_-1]: #자기 냄새 있는 곳 중 우선순위
                ndir_ = j
                nr = r + move[ndir_][0]
                nc = c + move[ndir_][1]
                if nr in [-1,n] or nc in [-1,n]:
                    continue
                if map_[nr][nc][0] == i:
                    break
                           
        #상어 정보 최신화
        shark_loc[i] = [nr,nc]
        shark_dir[i] = ndir_

        
        if [nr,nc] in move_loc: #상어 겹칠 때
            shark_list_tmp.remove(i)
            continue

        move_loc.append([nr,nc])
        move_loc_info.append([i,nr,nc])

    shark_list = shark_list_tmp 
    
    for r in range(n): #냄새 1씩 줄이기
        for c in range(n):
            if map_[r][c] != [0,0]:
                map_[r][c][1] -= 1
                if map_[r][c][1] == 0:
                    map_[r][c] = [0,0]
                    
    for num,r,c in move_loc_info: #새로 도착한 곳에 냄새 정보 최신화
        map_[r][c] = [num,k]

    if len(shark_list) == 1: #1번 상어만 남았을 때
        break

print(cnt)