n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

#dfs를 정의내린 이유 -> 퍼진 바이러스 계산하기 위해
def dfs(x,y,data) :
    for i in range(4): #상하좌우
        nx = x+dx[i]
        ny = y+dy[i]
        if not (x>=n or x<0 or y>=m or y<0): #범위일 때
        
            if data[nx][ny] == 0: #0이면 1이 나올때까지 바이러스퍼뜨림
                data[nx][ny] = 2
                dfs(nx,ny) 

    return data

#울타리를 3개씩 설치하는 모든 방법 -> 위의 dfs에 넣고 0갯수 count
# def dfs2()
#     count = 0
#     for i in range(n):
#         for j in range(m):
#             if dfs(i,j): #0을 count한값을 result에 추가
#                 count +=1
#     print(count)