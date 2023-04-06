import sys
from heapq import heappush, heappop, heapify


def input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())
    cards = [int(input()) for _ in range(N)]
    # 원래 있던 리스트로 힙큐 만들기
    heapify(cards)
    
    answer = 0

    while len(cards) != 1:
        # 가장 작은거 두 개 꺼내서 더하고 다시 큐에 넣기
        add1 = heappop(cards)
        add2 = heappop(cards)
        res = add1 + add2
        heappush(cards, res)
        answer += res

    print(answer)

# 백준 정답, 메모리 : 119176 KB, 시간 : 280 ms