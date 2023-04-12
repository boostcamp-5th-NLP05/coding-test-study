import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
triangle = [[] for i in range(N)]
for i in range(N):
    triangle[i] = list(map(int, input().split()))

dp = [[0 for c in range(len(triangle[r]))] for r in range(N)]


# 행 단위로 내려가면서 각 열 위치에서 최대값을 찾는다.
for r in range(N):
    for j in range(len(triangle[r])):

        # 첫 번째 면 그대로.
        if j == 0:
            dp[r][j] = triangle[r][j] + dp[r-1][0]

        # 마지막 열도 그대로.
        elif j == len(triangle[r]) - 1:
            dp[r][j] = triangle[r][j] + dp[r - 1][len(triangle[r-1]) - 1]

        # 그 외 -> 왼쪽 위, 오른쪽 위 중 큰 값을 더해주면 됨.
        else:
            dp[r][j] = triangle[r][j] + max(dp[r-1][j-1], dp[r-1][j])


answer = 0

# 마지막 행에서 최댓값 찾기
for i in range(N):
    answer = max(answer, dp[N-1][i])

print(answer)
