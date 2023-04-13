import sys


def input():
    return sys.stdin.readline().rstrip()

        
if __name__ == "__main__":
    N = int(input())
    warriors = list(map(int, input().split()))
    in_list = [True] * N

    # dp[i]: i번째 병사를 마지막으로 끝나는 최대 부분 수열의 길이
    dp = [1] * N

    # 병사 i 앞에 있는 병사 j들 중에서 i보다 전투력이 큰 병사 뒤에 붙기
    for i in range(1, N):
        for j in range(i):
            if warriors[j] > warriors[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(N - max(dp))

