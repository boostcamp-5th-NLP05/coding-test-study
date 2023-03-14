N = int(input())
coin = list(map(int, input().split()))

coin.sort()

start = 1
for c in coin:
    # start: c보다 작은 동전들로 못 만드는 값의 최소.
    if start < c:
        break
    start = start + c

print(start)
