# 백준 10825 정답, 53896 KB, 504 ms, Python3
import sys
from functools import cmp_to_key

N = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(N):
    name, kor, eng, math = sys.stdin.readline().rstrip().split()
    arr.append((name, int(kor), int(eng), int(math)))


def cmpare(x, y):
    # 음수를 반환하면 순서는 x->y
    if x[1] == y[1]:
        if x[2] == y[2]:
            if x[3] == y[3]:
                return -1 if x[0] < y[0] else 1
            return y[3] - x[3]  # 수학 내림차순
        return x[2] - y[2]  # 영어 오름차순
    return y[1] - x[1]  # 국어 내림차순


arr.sort(key=cmp_to_key(cmpare))

for x in arr:
    print(x[0])
