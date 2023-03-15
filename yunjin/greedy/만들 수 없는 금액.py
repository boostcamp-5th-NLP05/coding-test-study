N = int(input())
numbers = list(map(int, input().split()))

# 최솟값부터 확인한다.
numbers.sort()

idx = 0

# 1 부터 시작해서 만들 수 있는지 검증해 나갈 수
start_number = 1

# 최소 단위로 조합하면서 만들 수 있는 금액을 채워나간다.
# check_list 는 numbers 의 최솟값을 numbers의 누적 조합에 계속 더해주는 것임.
check_list = []

# 시간복잡도 N^2 = 1000*1000 = 1000000  ?
while True:

    x = check_list.copy()

    # 누적 조합에 numbers[idx] 일괄 더해주기
    for i in range(len(x)):
        x[i] += numbers[idx]

    # 아무것도 안 더한 값두 더해줘야 한다.
    check_list.append(numbers[idx])

    check_list = check_list + x


    # check_list 에서 검증해간다.
    # 존재하지 않는다면 확인 끝.
    if start_number not in set(check_list):
        print(start_number)
        break

    # 존재한다면 새로운 조합을 만들어야 한다.
    # numbers 우측으로 한칸이동, start_number 1 증가.
    else:
        idx += 1
        start_number += 1

        # idx 가 len(numbers) 까지 갔다는 것은 모든 조합을 check_list 에 넣어줬다는 것이다. -> 반복문 탈출해서 검증만 돌면 된다.
        if idx == len(numbers):
            break

# 이제 check_list를 만들어 가는 것은 하지 않고 start_number를 검증하는 것만 한다.
# 시간 복잡도 O(1) ?
while True:
    if start_number not in set(check_list):
        print(start_number)
        break
    else:
        start_number += 1




