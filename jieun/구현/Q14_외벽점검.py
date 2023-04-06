import itertools


def solution(n, weak, dist):
    answer = 100 # 답이 될 수 없는 값으로 초기화
    weak_len = len(weak)

    def find_end(d, sidx, visited):
        # weak[sidx]에서 출발해서 시계방향으로 d 거리 안에 갈 수 없는 첫 취약점 반환
        # 취약점 방문하면 visited True로 채우기
        visited[sidx] = True
        nidx = sidx 
        while True:
            nidx = (nidx + 1) % weak_len  # 다음에 갈 취약점 인덱스
            if (weak[nidx] - weak[sidx] + n) % n > d or visited[nidx]:
                # d 거리보다 멀거나, 이미 방문한 취약점이면 바로 반환
                return nidx
            visited[nidx] = True # 방문 기록

    for order in itertools.permutations(dist): # 출발하는 순서의 모든 경우 탐색
        for start in range(weak_len): # 첫 출발점을 옮겨가면서 탐색
            visited = {i: False for i in range(weak_len)}  # 방문 여부. weak의 인덱스를 원소로 가짐
            cnt = 0
            sidx = start # 출발점
            for d in order:
                # weak[sidx]에서 거리 d 내에 있는 취약점 방문.
                eidx = find_end(d, sidx, visited) # 방문하지 못 하는 첫 취약점
                cnt += 1
                if visited[eidx]: # 모든 취약점을 다 방문함
                    answer = min(answer, cnt)
                    break
                sidx = eidx

    if answer == 100:
        answer = -1
    return answer
