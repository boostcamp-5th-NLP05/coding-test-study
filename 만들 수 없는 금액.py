import itertools

def Solution():
    n = int(input())
    coin = list(map(int, input().split()))
    money_list = [0 for _ in range(sum(coin)+2)]
    money_list[0] = 1
    
    for i in range(1,n+1):
        comb = list(itertools.combinations(coin,i))#콤비네이션으로 모든 조합 찾기
        for j in comb:
            money_list[sum(j)] = 1
    
    for i in range(len(money_list)):
        if money_list[i] == 0: #모든 조합에서 안나온 숫자 찾기
            return i
        
Solution()