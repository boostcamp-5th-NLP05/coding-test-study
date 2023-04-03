import sys


def input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())

    students = []
    for _ in range(N):
        name, score = input().split()
        students.append([int(score), name])

    students.sort()

    for _, name in students:
        print(name, end=" ")
