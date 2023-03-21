if __name__ == "__main__":
    N = input()
    len_ = len(N)

    # 중간을 기준으로 리스트 양 옆으로 나누기
    left = N[: len_ // 2]
    right = N[len_ // 2 :]

    # 리스트에서 한 값씩 꺼내며 정수로 캐스팅하고, 새로운 리스트 만들어서 합 구하기
    left_sum = sum([int(c) for c in left])
    right_sum = sum([int(c) for c in right])

    # 조건 비교
    if left_sum == right_sum:
        print("LUCKY")
    else:
        print("READY")

    # 3분 40초
