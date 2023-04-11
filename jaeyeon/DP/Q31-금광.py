import sys


def input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        gold_list = list(map(int, input().split()))
        dp = [0] + gold_list

        # 열을 기준으로 왼쪽에서부터 업데이트
        for c in range(2, m + 1):
            # 왼쪽 값들을 보며 현재 값을 업데이트
            for r in range(0, n):
                if r == 0:
                    dp[r * m + c] += max(dp[r * m + c - 1], dp[(r + 1) * m + c - 1]) # 왼쪽 값, 왼쪽 아래 값 비교

                elif r == n - 1:
                    dp[r * m + c] += max(dp[(r - 1) * m + c - 1], dp[r * m + c - 1]) # 왼쪽 위 값, 왼쪽 값 비교

                else:
                    dp[r * m + c] += max(dp[(r - 1) * m + c - 1], dp[r * m + c - 1], dp[(r + 1) * m + c - 1])
                    # 왼쪽 아래 값, 왼쪽 값, 왼쪽 아래 값 비교

        # 마지막 열만 보기
        last_column = [dp[r * m] for r in range(1, n + 1)]

        print(max(last_column))

# 37분 40초
