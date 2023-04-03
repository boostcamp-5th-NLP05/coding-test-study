N, K = map(int, input().split())

array_A = list(map(int, input().split()))
array_B = list(map(int, input().split()))

# 정렬
array_A.sort()
array_B.sort()

answer = sum(array_A)
for i in range(K):

    # A는 왼쪽에서 B는 오른쪽에서 접근하면서 원소 바꾸면서 더해줌.
    left = array_A[i]
    right = array_B[N - 1 - i]

    if left < right:
        answer -= left
        answer += right
    else:
        break

print(answer)
