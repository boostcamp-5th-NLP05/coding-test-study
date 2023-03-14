if __name__ == "__main__":
    N = int(input())
    F_list = list(map(int, input().split()))

    F_list.sort(reverse=True)
    answer = 0
    idx = 0

    while idx < N:
        if idx + F_list[idx] <= N:
            idx += F_list[idx]
            answer += 1
        else:
            idx += 1
            continue

    print(answer)
