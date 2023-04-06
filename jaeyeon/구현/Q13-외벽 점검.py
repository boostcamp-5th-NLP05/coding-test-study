answer = -1


def dfs(n, clear, weak, dist, dist_done, start, depth):
    global answer

    if False not in dist_done:
        return

    # 현재 위치 외벽 점검하기
    clear[start] = True
    for i in range(len(dist)):
        if dist_done[i]:
            continue
        # dist 사용 표시
        dist_done[i] = True

        cur_dist = dist[i]

        # 원복을 위해 점검한 외벽 체크
        changed = []
        cur_pos = start

        # 외벽 점검
        for _ in range(cur_dist):
            next_pos = (cur_pos + 1) % n
            if not clear[next_pos]:
                changed.append(next_pos)
                clear[next_pos] = True
            cur_pos = next_pos

        if False not in clear:
            # 모든 외벽이 점검된 것
            if answer == -1:
                answer = depth
            else:
                answer = min(answer, depth)

        # 다음 dist로 dfs 진행
        for w in weak:
            if not clear[w]:
                dfs(n, clear, weak, dist, dist_done, w, depth + 1)
                break

        # 점검 상태 복구
        for c in changed:
            clear[c] = False

        # dist 원상태 복구
        dist_done[i] = False

    # 현재 위치 외벽 점검 취소
    clear[start] = False


def solution(n, weak, dist):
    global answer

    # 가장 멀리 갈 수 있는 친구 먼저 보내기
    dist.sort(reverse=True)

    # 외벽 점검 상태를 확인하는 배열
    clear = [False if w in weak else True for w in range(n)]

    # 친구가 나갔는지 확인하는 배열
    dist_done = [False for _ in range(len(dist))]

    # 맨 처음 출발지는 모든 weak에 대해서 실행
    for w in weak:
        dfs(n, clear, weak, dist, dist_done, w, 1)

    return answer


# 고려해야 할 것
# (1)어떤 친구를 (2)어디서 보낼지


if __name__ == "__main__":
    n = 12
    weak = [1, 5, 6, 10]
    dist = [1, 2, 3, 4]

    print(solution(n, weak, dist))
