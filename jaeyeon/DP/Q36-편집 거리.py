import sys
from collections import Counter, defaultdict


def input():
    return sys.stdin.readline().rstrip()


def remove_lcs(a, b):
    A = "-" + a
    B = "-" + b

    dp = [[0] * (len(A)) for _ in range(len(B))]

    for i in range(1, len(B)):
        for j in range(1, len(A)):
            if A[j] == B[i]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    i = len(B) - 1
    j = len(A) - 1
    lcs_A = []
    lcs_B = []
    lcs = ''
    while i > 0 and j > 0:
        if dp[i][j] == dp[i][j - 1]:
            j -= 1
        elif dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            lcs = A[j] + lcs
            lcs_A.append(j)
            lcs_B.append(i)
            i -= 1
            j -= 1

    # 각 문장별로 lcs의 인덱스가 담긴 배열 만들기
    lcs_A = lcs_A[::-1]
    lcs_B = lcs_B[::-1]

    # 연산 횟수
    count = 0

    # lcs를 제외하고 나서 남은 부분 문자열 쌍 저장
    removed = []

    for i in range(-1, len(lcs_A)):
        # lcs 사이에 있는 substring 쌍 구하기
        if i == len(lcs_A) - 1:
            sub_A = A[lcs_A[i]+1:]
            sub_B = B[lcs_B[i]+1:]
        elif i == -1:
            sub_A = A[1:lcs_A[i+1]]
            sub_B = B[1:lcs_B[i+1]]
        else:
            sub_A = A[lcs_A[i] + 1 : lcs_A[i + 1]]
            sub_B = B[lcs_B[i] + 1 : lcs_B[i + 1]]
        
        removed.append([sub_A, sub_B])

    return lcs, removed


if __name__ == "__main__":
    A = input()
    B = input()

    lcs, removed = remove_lcs(A, B)
    print(f'lcs : {lcs}')
    print(f'removed : {removed}')

    answer = 0
    for sub_A, sub_B in removed:
        # 각각의 문자열 쌍에는 겹치는 문자가 없으므로 삭제와 교체 연산을 통해 문자열을 같게 만들어야 한다.
        # 연산 횟수는 둘 중 더 긴 문자열과 같다.
        answer += max(len(sub_A), len(sub_B))

    print(answer)
