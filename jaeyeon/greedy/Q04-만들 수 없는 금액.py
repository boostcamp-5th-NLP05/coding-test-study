if __name__=="__main__":
    N = int(input())
    coins = list(map(int, input().split()))
    
    coins.sort(reverse=True)
    answer = 0

    # 만들어야 하는 숫자
    target = 1
    while True:
        isAble = False      # 만들 수 있는지 알려줄 flag
        money = 0           # 현재 코인의 합을 저장

        for coin in coins:  # 코인이 큰 순서부터 money에 더하기
            if coin + money > target:
                continue
            elif coin + money == target:
                isAble = True
                break
            else:
                money += coin
        
        if not isAble:      # isAble을 통해 만들 수 있는지 없는지 판단
            answer = target
            break
        target += 1

    print(answer)