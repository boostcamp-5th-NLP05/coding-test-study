from collections import deque

n, k = map(int,input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

s,x,y = map(int,input().split())

#################################################입력

queue = deque([(x-1,y-1,0)]) #(x,y) 부터 시작
move = [[1,0], [-1,0], [0,1], [0,-1]]

answer = []

if data[x-1][y-1] != 0: #x,y가 시작부터 0이 아닌 케이스가 있어서
    answer.append(data[x-1][y-1])
data[x-1][y-1] = -1

check_time = -1 #시간이 지나는 순간 알기 위한 변수
while queue:
    r,c,cnt = queue.popleft()
    
    if cnt != check_time and len(answer) != 0: #시간이 지났을 때 answer에 추가된 것이 있다면 조기 종료 
        break

    if cnt == s: #s초가 지났을 때 종료
        break

    for i in move:
        nr = r + i[0]
        nc = c + i[1]
        
        if nr in [-1,n] or nc in [-1,n]: #범위 밖
            continue

        if data[nr][nc] > 0: #바이러스를 만났을 때
            answer.append(data[nr][nc])
            data[nr][nc] = -1
            continue

        if data[nr][nc] == 0:
            data[nr][nc] = -1
            queue.append([nr,nc,cnt+1])

    check_time = cnt #시간 체크

if len(answer) == 0: #종료 이후 answer에 추가된 것이 없으면 0
    print(0)
else:
    print(min(answer)) #answer에 추가된 것 중에 가장 작은 바이러스 반환 