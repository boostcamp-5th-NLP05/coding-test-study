import sys
import bisect


def input():
    return sys.stdin.readline().rstrip()


def check_cut(ricecakes, idx, cut_val):
    ret = 0
    # ricecakes[idx:]에는 cut_val보다 긴 떡만 담긴다
    for ricecake in ricecakes[idx:]:
        ret += ricecake - cut_val
    return ret


def binary_search(ricecakes, items, M, start, end):
    while start < end:
        # 절단기의 높이
        mid = (start + end) // 2

        # 떡 중에서 절단기의 높이보다 높은 떡의 가장 첫번째 인덱스 구하기
        cut_idx = bisect.bisect(ricecakes, items[mid])

        # 현재 절단기의 높이로 잘랐을 때 얻을 수 있는 떡볶이 길이
        cut_val = check_cut(ricecakes, cut_idx, items[mid])

        # 떡을 M만큼 얻으면서 가장 높은 높이를 구해야하므로 upper bound 구하기
        if cut_val >= M:
            start = mid + 1
        else:
            end = mid
    return end


if __name__ == "__main__":
    N, M = map(int, input().split())
    ricecakes = list(map(int, input().split()))
    ricecakes.sort()

    # 절단기의 높이 범위를 담아둔 배열
    items = list(range(1, max(ricecakes) + 1))
    print(binary_search(ricecakes, items, M, 0, len(items) - 1))
