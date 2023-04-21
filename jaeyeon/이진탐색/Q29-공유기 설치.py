import sys


def binary_search(homes, start, end):
    ret = 0
    while start <= end:
        mid = (start + end) // 2
        val = homes[0]
        count = 1
        for i in range(1, len(homes)):
            if homes[i] >= val + mid:
                val = homes[i]
                count += 1
        if count >= C:
            start = mid + 1
            ret = mid
        else:
            end = mid - 1
    return ret


def input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N, C = map(int, input().split())
    homes = []
    for _ in range(N):
        homes.append(int(input()))
    homes.sort()

    print(binary_search(homes, 0, homes[-1] - homes[0]))
