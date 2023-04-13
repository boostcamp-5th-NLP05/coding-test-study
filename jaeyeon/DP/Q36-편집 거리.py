import sys
from collections import Counter, defaultdict


def input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    A = input()
    B = input()

    # 캐릭터 별로 개수 세기
    list_A = Counter(A)
    list_B = Counter(B)

    # 캐릭터 별 숫자 차이 세기
    total = defaultdict(int)
    for c in list_A:
        total[c] = list_A[c]

    for c in list_B:
        total[c] -= list_B[c]

    # total의 요소 값이 0보다 크면 A에 더 많은 캐릭터, 0보다 작으면 B에 더 많은 캐릭터라는 뜻
    answer = 0
    for c in total:
        answer += total[c]

    print(abs(answer))
