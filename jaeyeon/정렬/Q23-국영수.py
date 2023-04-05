import sys


def input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())
    scores = []
    for _ in range(N):
        name, lang, eng, math = input().split()
        scores.append([name, int(lang), int(eng), int(math)])

    # 조건에 맞게 내림차순은 (-)로, 오름차순은 (+)로 정렬
    scores.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

    for name, _, _, _ in scores:
        print(name)

# 백준 정답, 메모리 : 151965 KB, 시간 : 648 ms