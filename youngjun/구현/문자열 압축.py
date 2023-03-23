def solution(s):
    answer = []
    
    if len(s) == 1: #한글자면 리턴 1로 끝내기
        return 1

    for i in range(1,len(s)//2+1): #1개 단위부터 끊어서 유닛에 append
        units = []

        for j in range(0,len(s),i):
            units.append(s[j:j+i])      #인덱싱할 때 맨 뒤는 범위 넘어가도 에러가 안 걸리는걸 처음 앎

        result = ''
        cnt = 1
        final = False
        
        for k in range(len(units)-1):    
            if units[k] == units[k+1]:   #units행렬에서 뒤와 같은 것을 찾음
                cnt += 1
                if k+1 == len(units) -1: #반복문의 range 가 len(units-1) 이라 마지막은 따로 체크해줘야 함
                    result += str(cnt) + units[k]
                    final = True
            else:
                if cnt == 1:
                    result += units[k]
                else:
                    result += str(cnt) + units[k]
                    cnt = 1

        if not final: #마지막이 전과 같지 않다면 그냥 이어 붙이기
            result += units[-1]
            final = False
        
        answer.append(len(result)) #단위별로 길이를 answer에 append

    return min(answer)
#23분 17초