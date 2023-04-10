x = int(input())

d = [0] * (x+1) #d에 들어갈 것 : x부터 시작해서 각 숫자에 도달할때까지 연산 횟수

for i in range(2, x+1):
    d[i] = d[i-1] + 1 #먼저 1을 더한 값을 넣어주고 비교
    if i % 5 == 0:
        d[i] = min(d[i],d[i//5]+1)
    if i % 3 == 0:
        d[i] = min(d[i],d[i//3]+1)
    if i % 2 == 0:
        d[i] = min(d[i],d[i//2]+1)
     
print(d[x])
