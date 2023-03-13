if __name__=="__main__":
    N, M, K = map(int, input().split())
    data = list(map(int, input().split()))

    data.sort(reverse=True)

    answer = 0
    first = data[0]
    second = data[1]

    while M > 0:
        for _ in range(K):
            if M == 0: break
            answer += first
            M -= 1
        if M == 0: break
        answer += second
        M -= 1

    print(answer)
        
        