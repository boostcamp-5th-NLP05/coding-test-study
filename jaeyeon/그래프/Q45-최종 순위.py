import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


if __name__ == "__main__":
    T = int(input())
    answers = []
    for _ in range(T):
        n = int(input())
        indegree = [0] * (n + 1)
        graph = [[] for _ in range(n + 1)]
        last_year = list(map(int, input().split()))
        m = int(input())

        # 바뀌는게 없다면 바로 출력
        if m == 0:
            answers.append(last_year)

        else:
            changes = [list(map(int, input().split())) for _ in range(m)]

            for k in range(1, n + 1):
                for idx in range(k + 1, n + 1):
                    # 작년과 상대 순위가 달라진 경우
                    if [k, idx] in changes or [idx, k] in changes:
                        indegree[idx] += 1
                        graph[k].append(idx)

                    # 순위가 그대로인 경우
                    else:
                        indegree[k] += 1
                        graph[idx].append(k)

            # 위상 정렬 실행
            q = deque()
            for idx in range(1, n + 1):
                if indegree[idx] == 0:
                    q.append(idx)
            result = []
            while q:
                cur_idx = q.popleft()
                result.append(cur_idx)
                for node in graph[cur_idx]:
                    indegree[node] -= 1
                    if indegree[node] == 0:
                        q.append(node)

            if len(result) != n:
                answers.append(-1)
            else:
                answers.append(result)

    for answer in answers:
        if answer == -1:
            print("IMPOSSIBLE")
        else:
            for c in answer:
                print(c, end=" ")
            print()
