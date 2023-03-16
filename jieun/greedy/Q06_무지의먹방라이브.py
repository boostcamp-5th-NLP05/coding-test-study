from queue import PriorityQueue


def solution(food_times, k):

    # 먹는 시간 순 오름차순 우선순위 큐 생성
    que = PriorityQueue()
    for i, val in enumerate(food_times):
        que.put((val, i + 1))

    pre = 0
    n = len(food_times)
    answer = -1
    last = []
    while not que.empty():
        val, idx = que.get()
        t = n * (val - pre)
        if t <= k:
            # 필요시간이 같은 음식들의 개수를 구하고 que에서도 제거한다.
            same = 1
            while not que.empty() and que.queue[0][0] == val:
                que.get()
                same += 1

            n -= same
            pre = val
            k -= t
        else:
            # 남은 음식 queue를 list로 변환한다.
            last.extend(que.queue)
            last.append((val, idx))
            break

    # 남은 음식이 존재할 때
    if n > 0:
        last.sort(key=lambda x: x[1])
        answer = last[k % n][1]

    return answer
