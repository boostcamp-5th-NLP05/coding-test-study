
N = int(input())
data = [[0 for _ in range(N)] for _ in range(N)] # 보드 생성
K = int(input())
dx, dy = 0, 0 #뱀의 머리의 위치
data[dx][dy] = 2 #뱀의 머리의 위치는 2로 표시
temp_dir = "E" # 현재 이동방향은 동쪽
count = 0 #걸린 시간
snake_loc = [(0,0)] #뱀이 차지하는 위치들
br = 'nonstop' # 이중for문 빠져나오기 위한 변수추가
for k in range(K):
    i, j = map(int, input().split())
    data[i-1][j-1] = 1 #사과의 위치에 1
L = int(input())
num_list = []
dir_list = []
for l in range(L):
    num, dir = input().split()
    num = int(num)
    num_list.append(num)
    dir_list.append(dir)
#게임시작으로부터 num초뒤 바뀌는 방향이 dir이므로 step으로 취급하기 위해 빼줌
for nn in range(len(num_list)-1,0,-1):
    num_list[nn] = num_list[nn]-num_list[nn-1]

for num in range(len(num_list)):    
    dir = dir_list[num]
    for n in range(num_list[num]):
        bx, by = dx, dy #이전 위치 미리 저장
        if temp_dir == "N":
            dx -= 1
        elif temp_dir == "E":
            dy += 1
        elif temp_dir == "S":
            dx += 1
        else:
            dy -= 1
        count+=1
        if dx <0 or dx>=len(data) or dy <0 or dy>=len(data[0]) or data[dx][dy] ==2:
            print(count)
            br = 'stop'
            break                   
        if data[dx][dy] != 1: #사과가 없다면
            data[snake_loc[0][0]][snake_loc[0][1]] = 0 #꼬리 자르기
            snake_loc.pop(0)
        data[dx][dy] = 2
        snake_loc.append((dx,dy))
        
    if br == 'stop':
        break
    #방향 바꾸기
    if temp_dir == "N" and dir == "L":
        temp_dir = "W"
    elif temp_dir == "E" and dir == "L":
        temp_dir = "N"
    elif temp_dir == "S" and dir == "L":
        temp_dir = "E"
    elif temp_dir == "W" and dir == "L":
        temp_dir = "S"
    elif temp_dir == "N" and dir == "D":
        temp_dir = "E"
    elif temp_dir == "E" and dir == "D":
        temp_dir = "S"
    elif temp_dir == "S" and dir == "D":
        temp_dir = "W"
    else:
        temp_dir = "N"

if br == "nonstop":
    print(count)

