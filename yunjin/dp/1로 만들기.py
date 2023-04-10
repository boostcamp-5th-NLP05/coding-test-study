import sys
input = sys.stdin.readline

N = int(input())

dp = [0 for i in range(N+1)]

dp[0] = 0
dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 1

for i in range(6, N+1):
    if i % 5 == 0:
        dp[i] = min(dp[i-1], dp[i//5]) + 1
    elif i % 3 == 0:
        dp[i] = min(dp[i-1], dp[i//3]) + 1
    elif i % 2 == 0:
        dp[i] = min(dp[i-1], dp[i//2]) + 1
    else:
        dp[i] = dp[i-1] + 1

print(dp[N])