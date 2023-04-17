import sys
import bisect

input = sys.stdin.readline

N, x = map(int, input().split())

numbers = list(map(int, input().split()))

# bisect
answer = bisect.bisect_right(numbers, x) - bisect.bisect_left(numbers, x)

if answer > 0:
    print(answer)
else:
    print(-1)
