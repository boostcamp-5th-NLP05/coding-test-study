import sys


def input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N, K = map(int, input().split())
    list_A = list(map(int, input().split()))
    list_B = list(map(int, input().split()))
    list_A.sort()
    list_B.sort(reverse=True)

    for idx in range(K):
        if list_A[idx] > list_B[idx]:
            break
        list_A[idx], list_B[idx] = list_B[idx], list_A[idx]

    print(sum(list_A))
