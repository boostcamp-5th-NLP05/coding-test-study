import heapq


def solution(food_times, k):
    answer = 0

    h = []

    for idx, value in enumerate(food_times):
        heapq.heappush(h, (value, idx + 1))

    leave_food_size = len(food_times)
    gap = 0
    pre_mount = 0
    now_mount = 0

    if sum(food_times) <= k:
        return -1

    while True:

        now_mount = h[0][0]
        gap = now_mount - pre_mount

        if k < len(h) * gap:
            break
        if not h:
            break

        k -= len(h) * gap
        leave_food_size = len(h)
        pre_mount = h[0][0]
        heapq.heappop(h)

    k %= len(h)

    h.sort(key=lambda x: x[1])
    answer = h[k][1]

    return answer
