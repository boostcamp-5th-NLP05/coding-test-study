import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
soldiers = list(map(int, input().split()))
soldiers.insert(0, 0)

dp = [1 for i in range(2001)]
dp[0] = 0
dp[1] = 1


for i in range(2, N + 1):

    # 새롭게 추가되는 병사 기준으로 왼쪽으로 반복문을 진행하면서 dp 를 갱신해나간다.
    for j in range(1, i + 1):
        if soldiers[i - j] <= soldiers[i]:  # 뒤쪽 군인이 군사력이 더 크다면 오름차순이 되므로 체크 안함.
            continue
        else:  # 정상 내림차순인 경우 해당 지점의 dp와 비교.
            dp[i] = max(dp[i], dp[i - j] + 1)

# 각 지점의 dp 가 가지고 있는 값은 최대 내림차순 길이이므로 max 값을 때주면 최소 열외 인원을 구할 수 있음.
print(N - max(dp))
