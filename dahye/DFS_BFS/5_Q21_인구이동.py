from collections import deque
import copy 

N, L, R = map(int,input().split())
data = []
for i in range(N):
    data.append(list(map(int,input().split())))

#상하좌우로 이동하면서 연합이 가능한 나라 저장
def bfs(x1,y1) :
    global check_list, data
    dx = [-1, 1, 0, 0] #상하좌우로 이동
    dy = [0, 0, 1, -1]
    queue = deque([(x1,y1)])
    union_list = [[x1,y1]] #나중에 나라 인구수 update해줄때 필요한 list
    union_sum = data[x1][y1] #총 인구수 합
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>=N or nx<0 or ny>=N or ny<0: #범위가 아닐 때
                continue
            if abs(data[nx][ny] - data[x][y])>=L and abs(data[nx][ny] - data[x][y])<=R and check_list[nx][ny] == 0: #차가 범위 안이고 아직 연합이 아닌 도시라면
                union_list.append([nx,ny])
                queue.append((nx,ny))
                union_sum += data[nx][ny]
                check_list[nx][ny] = 1
    #한 연합 결성 완료 -> 업데이트
    for temp in union_list:
        ti,tj = temp 
        data[ti][tj] = union_sum//len(union_list)

data_temp = copy.deepcopy(data)
data_list = [data_temp] #인구이동 여부 확인 list 
count = 0
while True: 
    check_list = [[0 for _ in range(N)] for _ in range(N)] #모든 연합을 한번에 업데이트 해야하므로 연합에 들어갔는지 확인하는 list
    for i in range(N): 
        for j in range(N):
            if check_list[i][j] == 0: 
                bfs(i,j) #연합만들기
    data_temp = copy.deepcopy(data)
    print(data_list)

    data_list.append(data_temp)
    if data_list[-1] == data_list[-2] : #인구이동이 없을 때
        break
    # if count == 12:
    #     break while문이 break가 안되어 임시추가 (그래도 break가 안됨...)

    count += 1
print(count)



