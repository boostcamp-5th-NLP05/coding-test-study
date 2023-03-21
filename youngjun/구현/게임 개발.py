def solution():
    n,m = map(int, input().split())
    start = list(map(int, input().split()))
    
    map_ = []
    for _ in range(n):
        map_.append(list(map(int, input().split())))
############################################################        입력값 받기

    visit = [[0 for _ in range(m)] for _ in range(n)]             #가본 곳 표시할 list
    
    move = [[0,1],[1,0],[0,-1],[-1,0]]                             #북동남서 이동할 때 x,y 변화량
    
    x = start[1] #X 좌표
    y = start[0] #Y 좌표
    di = start[2] #방향
    
    visit[y][x] = 1
    
    while True:
        cnt = 0
        for _ in range(4):                                        #왼쪽부터 4방향 보기(1단계)
            cnt += 1                                              #총 확인 횟수
            di -= 1                                               #왼쪽부터 확인
            
            if di == -1:                                          #북에서 서 볼때
                di = 3

            dx = x + move[di][0]                                  #확인해볼 x좌표
            dy = y + move[di][1]                                  #확인해볼 y좌표
            

            if dx >= m or dx < 0 or dy >= n or dy < 0:          #확인한 곳이 지도 밖일 때 (2단계)
                continue
            
            if map_[dy][dx] == 0 and visit[dy][dx] == 0:         #확인한 곳이 갈 수 있는 곳일 때 (2단계)
                x = dx                                            #x좌표 갱신
                y = dy                                            #y좌표 갱신
                visit[y][x] = 1                                   #방문 표시
                cnt = 0                                           #cnt 초기화
                break                                             #1단계로
                
                                                  
        if cnt == 4:                                               #4방향 다 봤을 때
            x = x - move[di][0]                                    #뒤로 이동 (3단계)
            y = y - move[di][1] 
                                                
        if x >= m or x < 0 or y >= n or y < 0:                   #뒤로 이동했을 때 이동 못한다면 행동 끝 (3단계)
            break

        if map_[y][x] == 1:                                       #뒤로 이동했을 때 산이라면 행동 끝 (3단계)
            break
                                                                   #break문에 안걸렸을 시 while문을 통해 다시 1단계로
    answer = 0

    for i in visit:                                               #visit에 표시된 1 더하기
        answer += sum(i)

    return answer

solution()