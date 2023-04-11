N,M = map(int, input().split())
coin = []
for _ in range(N):
    coin.append(int(input()))

INF = 30000    
dp = [INF] * (M+1)
dp[0] = 0

for i in range(1, M+1):
    for c in coin: 
        if i-c >= 0: # 화폐 단위 c 사용 가능
            dp[i] = min(dp[i], dp[i-c]+1)
            
if dp[M] == INF: print(-1)
else: print(dp[M])