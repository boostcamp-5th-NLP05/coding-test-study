import sys
import heapq

input = sys.stdin.readline

n = int(input())
cards = []
for i in range(n):
    heapq.heappush(cards, int(input()))

result = 0

if len(cards) == 1:
    print(result)

else:
    for i in range(n - 1):  # 2개씩 꺼내기 떄문에 n-1
        previous = heapq.heappop(cards)
        current = heapq.heappop(cards)

        result += previous + current
        heapq.heappush(cards, previous + current)

    print(result)