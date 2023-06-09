N = int(input())

postions = list(map(int, input().split()))

postions.sort()

answer = sum(postions)
left_number_idx = 0

r = []

for position in postions:
    answer -= (N - left_number_idx) * position # 오른쪽으로 갈 때마다 감소하는 거리
    answer += left_number_idx * position # 오른쪽으로 갈 때마다 증가하는 거리
    left_number_idx += 1  # 왼쪽 갯수 증가
    r.append((answer, position))

r.sort(key=lambda x: (x[0], x[1]))
print(min(r)[1])

# 백준 정답, 메모리 : 75684 KB, 시간 : 336ms