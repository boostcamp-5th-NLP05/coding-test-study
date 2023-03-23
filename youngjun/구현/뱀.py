n = int(input()) #보드크기
k = int(input()) #사과 개수

map_= [[0]*(n+1) for _ in range(n+1)] # 좌표가 1,1 부터 시작이라 n+1로 생성

for _ in range(k):
    a, b = map(int,input().split()) #사과 위치
    map_[a][b] = 1

time_turn = []
l = int(input()) #방향 횟수
for _ in range(l):
    x, c = input().split()  #x초 c가 L이면 왼쪽 C가 D면 오른쪽
    time_turn.append([int(x), c])
    
move = [[0,1],[1,0],[0,-1],[-1,0]] #동 남 서 북

time = 0
turn_cnt = 0 #방향 바꾸는 시간 확인용
r,c = 1,1 #첫 시작 좌표
move_dir = 0 #방향
tail = [[1,1]] #몸통 표시할 리스트

while True:

    time += 1
    
    #방향으로 머리 늘려주기
    r += move[move_dir][0]               
    c += move[move_dir][1]
    
    #머리 늘린곳 tail에 추가
    tail.append([r,c])
    
    #time이 되면 방향 바꾸기
    if turn_cnt < l:  #범위 에러 나서 넣어줌
        if time_turn[turn_cnt][0] == time:
            if time_turn[turn_cnt][1] == 'L':
                move_dir = (move_dir - 1) % 4 #L이면 왼쪽
                turn_cnt += 1
            else:
                move_dir = (move_dir + 1) % 4 #R이면 오른쪽
                turn_cnt += 1
    
    #벽에 부딪혔을 때
    if r <= 0 or c <= 0 or r > n or c > n:
        break

    #자신 몸과 부딪혔을 때
    if [r,c] in tail[0:-1]:
#        print(r,c,time)  확인용 print
#        print('break')   확인용 print
        break
    
    #사과 안먹었으면 꼬리 지우기
    if map_[r][c] == 0:
        tail.pop(0)
    else: #사과 먹었을 때는 꼬리칸 냅두고 사과 지우기
        map_[r][c] = 0
    
#    print(tail,time)      확인용 print

print(time)

#35분 45초