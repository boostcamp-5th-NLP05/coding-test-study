import sys


def input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())
    houses = list(map(int, input().split()))

    houses.sort()

    # 중앙값 찾기
    antenna_1 = houses[N // 2 - 1]
    antenna_2 = houses[N // 2]

    cnt_antenna_1 = 0
    for house in houses:
        cnt_antenna_1 += abs(antenna_1 - house)
    cnt_antenna_2 = 0
    for house in houses:
        cnt_antenna_2 += abs(antenna_2 - house)

    # 중앙값 비교해서 프린트하기  
    if cnt_antenna_1 > cnt_antenna_2:
        print(antenna_2)
    else:
        print(antenna_1)

# 백준 정답, 메모리 : 147312 KB, 시간 : 200 ms