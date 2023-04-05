import sys
import heapq as h

N = int(sys.stdin.readline().rstrip())
cards = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

cnt = 0
h.heapify(cards)  # cards를 min heap으로 변환
while len(cards) > 1:
    # 가장 작은 두 묶음을 더함
    new = h.heappop(cards) + h.heappop(cards)
    cnt += new
    h.heappush(cards, new)

print(cnt)
