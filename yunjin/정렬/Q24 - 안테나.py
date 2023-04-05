N = int(input())

postions = list(map(int, input().split()))

postions.sort()

answer = sum(postions)
left_number_idx = 0

r = []

for position in postions:
    answer -= (N - left_number_idx)
    answer += left_number_idx
    left_number_idx += 1  # 왼쪽 갯수 증가
    r.append((answer, position))

r.sort(key=lambda x: (x[0], x[1]))
print(min(r)[1])
