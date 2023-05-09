#map_ = [[],[],[],[]]
#for i in range(4):
#    tmp = list(map(int,input().split()))
#    for j in range(4):
#        map_[i].append((tmp[j*2],tmp[j*2 + 1]))
#map_ = [[(7, 6), (2, 3), (15, 6), (9, 8)], [(3, 1), (1, 8), (14, 7), (10, 1)], [(6, 1), (13, 6), (4, 3), (11, 4)], [(16, 1), (8, 7), (5, 2), (12, 2)]]
#map_ = [[(16, 7), (1, 4), (4, 3), (12, 8)], [(14, 7), (7, 6), (3, 4), (10, 2)], [(5, 2), (15, 2), (8, 3), (6, 4)], [(11, 8), (2, 4), (13, 5), (9, 4)]]
map_ = [[(12, 6), (14, 5), (4, 5), (6, 7)], [(15, 1), (11, 7), (3, 7), (7, 5)], [(10, 3), (8, 3), (16, 6), (1, 1)], [(5, 8), (2, 7), (13, 6), (9, 2)]]
#map_ = [[(-1, 0), (2, 4), (9, 3), (10, 1)], [(6, 1), (12, 2), (1, 8), (14, 7)], [(16, 1), (5, 2), (15, 6), (13, 1)], [(3, 4), (4, 3), (11, 4), (0, 7)]]
move = [(0,0),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
first_eat = map_[0][0][0]
shark_move = map_[0][0][1]
map_[0][0] = (0,shark_move)
shark_r = 0
shark_c = 0

def move_fish(fish_map):
    for num in range(1,17):
        tmp = False
        for r in range(4):
            if tmp:
                break
            for c in range(4):
                if tmp:
                    break
                    
                fish_num = fish_map[r][c][0]
                if fish_num == num:
                    move_idx = fish_map[r][c][1]
                    fish_move = move[move_idx]
                    nr = r + fish_move[0]
                    nc = c + fish_move[1]
                    
                    while nr in [-1,4] or nc in [-1,4] or fish_map[nr][nc][0] == 0: #벽에 막히거나 상어일 때
                        move_idx = (move_idx % 8) + 1 #각도 바꾸고
                        fish_move = move[move_idx]
                        nr = r + fish_move[0] #움직이기
                        nc = c + fish_move[1]
                        
                    move_info = fish_map[nr][nc] #위치 바꾸기
                    fish_map[nr][nc] = (fish_num,move_idx)
                    fish_map[r][c] = move_info
                    tmp = True

    return fish_map

import copy
global answer
answer = 0
fish_nums = [i for i in range(1,17)]

def DFS(shark_r,shark_c,shark_move,fish_map,cnt):
    global answer
    new_map = copy.deepcopy(fish_map)
    can_move = False
    
    for i in range(1,4):
        nr = shark_r + (move[shark_move][0]*i)
        nc = shark_c + (move[shark_move][1]*i)

        if nr < 0 or nc > 3 or nr < 0 or nr > 3:
            continue
    
        if new_map[nr][nc][0] not in fish_nums:
            continue

        new_move = new_map[nr][nc][1] #먹은 물고기의 방향
        cnt += new_map[nr][nc][0] #먹은 물고기 번호
        
        new_map[shark_r][shark_c] = (-1,0) #상어가 있던곳 빈공간 처리
        new_map[nr][nc] = (0,new_move) #상어가 도착한 곳 상어로 처리
        
        can_move = True
        
        new_map = move_fish(new_map) #먹었으면 물고기 움직이기
        print(cnt,new_map)
        DFS(nr,nc,shark_move,new_map,cnt) #먹은 위치에서 다시 반복
    
    if not can_move:
        answer = max(answer,cnt)

move_map = move_fish(map_)
DFS(0,0,shark_move,move_map,0)

print(answer)