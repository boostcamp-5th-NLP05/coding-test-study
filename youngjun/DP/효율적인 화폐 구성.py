n,m = map(int,input().split())
money = []

for _ in range(n):
    money.append(int(input()))

d = [-1] * 10001
d[0] = 0

for i in range(m):
    if d[i] == -1:
        continue
    
    for j in money:             #각 단위별로 더하기
        if d[i+j] == -1:        #처음 들어오는 것이 최소
            d[i+j] = d[i] + 1
            
    if d[m] != -1:              #값이 들어오면 break
        break

print(d[m])
