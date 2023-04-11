import sys


def input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N, M = map(int, input().split())
    money_list = [int(input()) for _ in range(N)]

    # 최소값 비교이므로 큰 값으로 dp 초기화
    INF = 987654321
    dp = [INF] * 10001

    for money in money_list:
        dp[money] = 1

    for i in range(min(money_list) + 1, M + 1):
        # 현재 보고 있는 값을 가지고 있는 동전으로 만들 수 있는 경우 구하기
        for money in money_list:
            try:
                dp[i] = min(dp[i], dp[i - money] + 1)
            except:
                continue

    if dp[M] == INF:
        print("-1")
    else:
        print(dp[M])
