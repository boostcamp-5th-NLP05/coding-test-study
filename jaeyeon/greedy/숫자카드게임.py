if __name__=="__main__":
    N, M = list(map(int, input().split()))
    min_list = []
    for _ in range(N):
        min_list.append(min(list(map(int, input().split()))))

    print(max(min_list))