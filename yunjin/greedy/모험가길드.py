N = int(input())
numbers = list(map(int, input().split()))

result = 0
x = []

# 공포도가 낮은 것 부터 처리해야 그룹을 최대한 나눌 수 있다.
numbers.sort()

for i in range(N):
    x.append(numbers[i])

    # 그룹에서 최대 공포가 인원수보다 작다면 그룹 수 증가하고 새로운 그룹 만들기 시도
    if len(x) >= max(x):
        result += 1
        x = []
        continue

print(result)
