def solution(food_times, k):
    answer = 0
    l = len(food_times)
    repeat = 0
    idx = 0

    # 1회 반복 전에 방송이 종료 된다면 k+1 리턴하고 종료
    if k < len(food_times):
        return k + 1

    while True:

        # 남아있는 음식 시간의 최솟값 * (먹어야할 음식의 갯수)
        if k <= l or k <= min(food_times) or k <= l * min(food_times):
            break

        # 먹는 시간이 가장 적게 걸리는 것을 다 먹었다는 것은
        # 반복문에서 큰 변화 없이 음식 먹는 일을 했다는 것.
        k -= l * min(food_times)
        idx = food_times.index(min(food_times))
        repeat = min(food_times)
        food_times[idx] = float("inf")  # 무한대로 바꿈. (최소값에서 체크하지 않기 위해서.)
        l -= 1
        print(food_times, k)

    # 음식배열에서 반복한 횟수를 빼주면 현 시점의 남은 음식 시간 배열을 구할 수 있다.
    for i in range(len(food_times)):
        food_times[i] -= repeat

    for i in range(len(food_times)):
        if food_times[i] == float("inf"):
            food_times[i] = 0

            # idx 를 0으로 초기화
    if k > 0:
        idx = 0

    # 이제 남은 k 를 0으로 만들면서 회전을 한다.
    while True:
        # print(food_times, idx, k)
        if food_times[idx] == 0:
            idx = (idx + 1) % len(food_times)
            continue
        else:
            food_times[idx] -= 1
            k -= 1
            idx = (idx + 1) % len(food_times)

            if k == 0:
                break

    # 다 먹었다면 불가하므로 -1 리턴한다.
    if sum(food_times) == 0:
        return -1

    # k = 0 인 상황에서 남은 음식을 찾는 과정
    while True:
        # print(food_times, idx, k)
        if food_times[idx] == 0:
            idx = (idx + 1) % len(food_times)
            continue
        else:
            return idx + 1


