if __name__ == "__main__":
    N, M = map(int, input().split())
    weights = list(map(int, input().split()))

    w_list = [0 for _ in range(M + 1)]  # 각 무게별로 볼링공의 개수를 센다
    for weight in weights:
        w_list[weight] += 1

    answer = N * (N - 1) // 2           # 볼링공 두 가지를 고르는 모든 경우의 수

    for w in w_list:                    # w_list를 순회하며, 무게가 같은 공이 2개 이상이면
        if w == 0 or w == 1:            # 그 공들 중에서 2개를 고르는 경우를 제외해준다.
            continue
        answer -= w * (w - 1) // 2
    print(answer)
