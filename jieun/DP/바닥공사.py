N = int(input())

MOD = 796796
# dp[i]: 가로 i인 바닥을 채우는 방법의 수
dp = [0] * (N+1)

dp[0] = 1
dp[1] = 1

for i in range(2, N+1):
    dp[i] = (dp[i-2] + dp[i-1] + dp[i-2]) % MOD
    # (1) dp[i-2]에 1x2 추가하는 경우
    # (2) dp[i-1]에 2x1 추가
    # (3) dp[i-2]에 2x2 추가
    
print(dp[N])