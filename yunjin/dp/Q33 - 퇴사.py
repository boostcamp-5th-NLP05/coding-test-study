import sys
def input():
    return sys.stdin.readline().rstrip()


N = int(input())
schedules = [list(map(int, input().split())) for i in range(N)]
schedules.insert(0, [0, 0])

dp = [0 for i in range(N + 1)]


# 이중 for문으로 날짜를 늘려가면서 최댓값을 갱신해나간다.
for i in range(1, len(schedules)):
    dp[i] = dp[i - 1]
    for j in range(1, i+1):
        if j + schedules[j][0] - 1 == i: # i번 째 날에 신규로 포함 시킬 수 있는 상담일에 대해서 dp 를 갱신 처리
            dp[i] = max(dp[i], dp[i - schedules[j][0]] + schedules[j][1])

print(dp[-1])
