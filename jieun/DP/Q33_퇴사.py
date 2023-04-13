# 백준 14501 정답: 31256 KB, 44 ms
N = int(input())
time = []
price = []
for _ in range(N):
    t, p = map(int, input().split())
    time.append(t)
    price.append(p)

dp = [0 for _ in range(N)]
# dp[i]: i일에 얻을 수 있는 최대 수익
# i일에 상담을 새로 시작하고, 선불로 받았을 때.

for i in range(N):
    for j in range(i):
        # i일 전에 상담이 끝나는 날짜만 고려
        if j + time[j] <= i:
            dp[i] = max(dp[i], dp[j])

    # i일에 시작한 상담이 퇴사 전까지 다 끝나는 경우만 선불로 받음
    if i + time[i] <= N:
        dp[i] += price[i]

ans = max(dp)
print(ans)
