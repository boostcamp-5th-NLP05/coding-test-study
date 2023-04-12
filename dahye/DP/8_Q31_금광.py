def gold(n,m,temp_data):
    data = []
    for t in range(n):
        data.append(list(temp_data[t*m:(t+1)*m])) #2차원 list로 바꿔줌
    for j in range(1, m):
        for i in range(n): #하나의 열씩 비교해야 하므로 다음과 같이 for문 작성
            if i == 0: #맨위와 맨아래는 두 방향에서 올 수 있음
                data[i][j] = data[i][j] + max(data[i][j-1],data[i+1][j-1]) 
            elif i == n-1:
                data[i][j] = data[i][j] + max(data[i-1][j-1],data[i][j-1])
            else:
                data[i][j] = data[i][j] + max(data[i-1][j-1],data[i][j-1],data[i+1][j-1])

    answer = 0
    for k in range(n): #마지막 열에서 가장 큰 값 출력
        answer = max(answer, data[k][m-1])

    return answer

ans = []
T = int(input())
for _ in range(T):
    n, m = map(int,input().split())
    data = list(map(int,input().split()))
    ans.append(gold(n,m,data))

for a in ans:
    print(a)
