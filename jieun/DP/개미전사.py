N = int(input())
food = list(map(int, input().split()))

dp = [0] * (N)
dp[0] = food[0]
dp[1] = max(food[0], food[1])

for i in range(1, N):
    dp[i] = max(dp[i - 1], dp[i - 2] + food[i])
    # (1) i 번째 창고를 포함하지 않는 경우
    # (2) i 번째 창고를 포함한 경우

print(dp[N - 1])
