N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))

# N : 주어지는 수의 개수
# M : 몇 개의 수자를 모을 것인가
# K : k 개 초과 불가

numbers.sort(reverse=True)

check = 0
loop = 0
r = []
while len(r) != M:
    check += 1
    r.append(numbers[loop])

    if loop == 1:
        loop = 0
        continue

    if check % K == 0:
        check = 0
        loop = 1


# print(numbers)
# print(r)
print(sum(r))
