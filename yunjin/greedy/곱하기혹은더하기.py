N = int(input())

numbers = list(map(int, str(N)))
result = 0

for i in range(len(numbers)):

    # 0 이라면 pass
    if numbers[i] == 0:
        continue

    # result 의 값이 0 이라면 값이 아닐 때 까지 더해준다.
    # 곱해주는 건 의미 없음
    if result == 0:
        result += numbers[i]
        continue

    plus_result = result + numbers[i]
    multi_result = result*numbers[i]

    # 더한게 더 크다면
    if plus_result >= multi_result:
        result = plus_result
    # 곱이 더 크다면
    else:
        result = multi_result

print(result)
