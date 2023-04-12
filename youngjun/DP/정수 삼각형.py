n = int(input())

tri = [[-1 for _ in range(n)] for _ in range(n)]
for i in range(n):
    num = list(map(int,input().split()))
    for j in range(len(num)):
        tri[i][j] = num[j]


d = [[0 for _ in range(n)] for _ in range(n)]

d[0][0] = tri[0][0] #dp 테이블 0,0 입력

for r in range(1,n):
    for c in range(0,n):
        if c == 0: #맨 왼쪽
            d[r][c] = d[r-1][c] + tri[r][c]
        elif c== n-1: #맨 오른쪽
            d[r][c] =  d[r-1][c-1] + tri[r][c]
        else:
            d[r][c] = max(d[r-1][c] + tri[r][c], d[r-1][c-1] + tri[r][c])

print(max(d[-1]))