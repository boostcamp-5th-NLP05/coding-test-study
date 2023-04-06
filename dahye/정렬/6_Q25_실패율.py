N = int(input())
stages = list(map(int, input().split()))

def solution(N, stages):
    answer = []
    failrate = dict() # 스테이지 번호와 실패율을 저장할 dic
    stages.sort()
    for i in range(1,N+1):
        if len(stages) == 0: #런타임에러로 인해 분모가 0일때 따로 처리
            failrate[i] = 0 
        else:
            failrate[i] = stages.count(i)/len(stages)
            stages = stages[stages.count(i):]
        #i번째 스테이지에서 실패한 사람 수/도전한 사람 수를 dic에 넣어줌
         #실패한 사람들 제외
    rate_sort = dict(sorted(failrate.items(), key = lambda x:x[1], reverse=True)) # value(실패율)를 기준으로 sort해줌
    answer = list(rate_sort.keys())

    return answer
print(solution(N, stages))