t = int(input())

gold = []
for _ in range(t):
    n, m = map(int,input().split())
    gold_ = list(map(int,input().split()))
    tmp = []
    for i in range(0,n*m,m): #입력 받은 1차원 리스트를 2차원 리스트로 변환
        tmp.append(gold_[i:i+m])
    gold.append(tmp)

inf = 10000000

for mine in gold:
    r, c = len(mine), len(mine[0])
    d = [[0 for _ in range(c)] for _ in range(r)]
    
    for i in range(r): #dp 테이블 첫번째 열 입력
        d[i][0] = mine[i][0]

    for i in range(1,c):
        for j in range(1,r):
            top,mid,bot = 0,0,0
            
            #위에서 오는 것
            if j == 0: #out of range
                top = -inf
            else:
                top = d[j-1][i-1]
            
            #정면으로 오는 것
            mid = d[j][i-1]
            
            #아래서 오는 것
            if j == r-1: #out of range
                bot = -inf
            else:
                bot = d[j+1][i-1]
            
            d[j][i] = max(top,mid,bot) + mine[j][i]
    

    last = [i[-1] for i in d]
    
    print(max(last))