n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int,input().split())))
if n == 1:
    print(data[0][0])
else:
    for i in range(n-2,-1,-1): #위층으로 올라가는 for문
        d = data[i] #d에 위층으로 올라갈때 최대를 저장하고 데이터에 저장하여 누적하는 방식
        for j in range(i+1): #위층에서 밑의 두수를 더한값중 큰 값을 d에 업데이트
            d[j] = max(data[i+1][j] + d[j], data[i+1][j+1] + d[j])
            data[i] = d # data 업데이트
    print(d[0])