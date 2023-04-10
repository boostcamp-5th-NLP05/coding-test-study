import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

r = []

answer = float('-inf')

# 한 지점을 기준으로 최대로 약탈가능한 것을 구한다.
for i in range(0, N - 2):
    lm = max(numbers[:i + 1])
    rm = max(numbers[i + 2:])
    answer = max(answer, lm + rm)

print(answer)