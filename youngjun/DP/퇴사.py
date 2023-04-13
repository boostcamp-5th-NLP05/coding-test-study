n = int(input())

schedule = []
for _ in range(n):
    schedule.append(list(map(int,input().split())))

d = [0] * (n+1)

for i in range(n-1, -1, -1): #n+1일 전에 끝나는 경우부터
    day, money = schedule[i]
    
    if i + day <= n:
        d[i] = max(d[i+day]+money,d[i+1])
    else:
        d[i] = d[i+1]


print(d[0])