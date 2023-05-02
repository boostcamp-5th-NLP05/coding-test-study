from collections import deque

N = int(input())

time = [0]  # 강의 시간
need_time = [0 for _ in range(N + 1)] # 수강하기까지 걸리는 최소 시간
ins = [0 for _ in range(N + 1)]  # 필요한 선수과목 개수
edges = [[] for _ in range(N + 1)] # 선수과목 -> 후속과목

for i in range(1, N + 1):
    line = map(int, input().split())
    time.append(next(line)) # line의 첫 번재 원소는 강의시간
    for l in line: # line의 두 번째 원소부터 시작
        if l == -1:
            break
        ins[i] += 1
        edges[l].append(i)  # l은 i의 선수과목

q = deque() # 큐로 사용
for i in range(1, N + 1):
    if ins[i] == 0:
        q.append(i)
        need_time[i] = time[i]

while q:
    cur = q.popleft()
    for nxt in edges[cur]:
        ins[nxt] -= 1
        need_time[nxt] = max(need_time[nxt], need_time[cur]) # 선수과목을 수강하기까지 걸리는 시간 중 최대
        if ins[nxt] == 0:
            q.append(nxt)
            need_time[nxt] += time[nxt]

for i in range(1, N + 1):
    print(need_time[i])
