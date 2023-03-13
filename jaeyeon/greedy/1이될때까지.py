if __name__=="__main__":
    N, K = list(map(int, input().split()))

    cnt = 0
    while N != 1:
        if N % K == 0:
            N /= K
            cnt += 1
        else:
            while N % K != 0:
                N -= 1
                cnt += 1
                
    print(cnt)