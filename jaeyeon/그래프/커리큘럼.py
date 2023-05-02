import sys
from collections import deque
from copy import deepcopy


def input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())

    # 위상 정렬을 진행하기 위한 배열 초기화
    indegree = [0] * (N + 1)
    graph = [[] for _ in range(N + 1)]

    # 강의별 최소 소요시간을 저장해둘 배열
    time = [0] * (N + 1)

    for cur in range(1, N + 1):
        row = list(map(int, input().split()))
        time[cur] = row[0]

        # (선이수과목 -> 현재 과목)의 edge 형태로 저장
        for pre in row[1:-1]:
            indegree[cur] += 1
            graph[pre].append(cur)

    # 위상 정렬 진행
    result = deepcopy(time)
    q = deque()

    # indegree가 0이라는 말은 선이수과목이 없다는 뜻. 위상 정렬을 위한 초기값으로 설정
    for idx in range(1, N + 1):
        if indegree[idx] == 0:
            q.append(idx)

    while q:
        cur = q.popleft()
        for i in graph[cur]:
            # 강의를 수강하는 데에 걸리는 최소 시간이므로 max 값만 저장
            result[i] = max(result[i], result[cur] + time[i])

            # 노드를 지우는 개념이므로 indegree 감소
            indegree[i] -= 1

            # indegree가 0이 된 과목은 큐에 넣어주기
            if indegree[i] == 0:
                q.append(i)

    for idx in range(1, N + 1):
        print(result[idx])
