import sys


def input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())
    foods = list(map(int, input().split()))

    # dp 배열 초기화
    dp = [0] * N
    dp[0] = foods[0]
    dp[1] = max(foods[0], foods[1])

    # 지금 음식과 2번째 전 음식을 택하는 경우,
    # 지금 음식을 포기하고 직전 음식을 택하는 경우 중 더 큰 수로 dp 업데이트
    for i in range(2, N):
        dp[i] = max(dp[i - 1], dp[i - 2] + foods[i])

    print(dp[N - 1])
