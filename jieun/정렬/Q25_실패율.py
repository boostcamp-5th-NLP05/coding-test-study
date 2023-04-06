def solution(N, stages):
    cnt = [0 for _ in range(N + 2)]  # 스테이지에 멈춰있는 플레이어 수
    for s in stages:
        cnt[s] += 1

    fail = [0] # 실패율
    for i in range(1, N + 1):
        a = sum(cnt[i:])  # 스테이지에 도달한 총 플레이어 수
        if a > 0.0:
            fail.append(cnt[i] / a)
        else:
            fail.append(cnt[i])

    answer = [x for x in range(1, N + 1)]
    answer.sort(key=lambda x: (-fail[x], x))

    return answer
