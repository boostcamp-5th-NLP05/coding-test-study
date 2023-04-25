import sys


def input():
    return sys.stdin.readline().rstrip()


INF = int(1e9)
if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [[INF] * (N + 1) for _ in range(N + 1)]

    # 그래프 초기값 설정
    for _ in range(M):
        src, dst = map(int, input().split())
        graph[src][dst] = 1

    for src in range(1, N + 1):
        for dst in range(1, N + 1):
            if src == dst:
                graph[src][dst] = 0

    # 플로이드 워셜 알고리즘 실행
    for k in range(1, N + 1):
        for src in range(1, N + 1):
            for dst in range(1, N + 1):
                graph[src][dst] = min(graph[src][dst], graph[src][k] + graph[k][dst])

    # 도달 횟수를 저장하기 위한 배열 생성
    reached = [0] * (N + 1)

    for src in range(1, N + 1):
        for dst in range(1, N + 1):
            if graph[src][dst] not in [0, INF]:
                reached[src] += 1  # 화살표의 시작
                reached[dst] += 1  # 화살표의 끝

    # 도달 횟수가 (N-1)번이면 순위를 정확히 알 수 있는 것
    print(reached.count(N - 1))
