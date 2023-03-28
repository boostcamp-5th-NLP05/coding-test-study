p = input()

def check(u): #올바른 괄호 문자 여부 확인 함수
    temp = 0
    for t in u:
        if t == '(':
            temp += 1
        else:
            temp -= 1
        if temp < 0:
            return False
    return True

#다시 수행해야 하는 재귀함수 생성
def solution(w):
    answer = ''
    if len(w) == 0:
        return answer
    #균형잡힌 문자열 u,v로 나누기
    for idx in range(1,len(w)+1):
        if w[:idx].count('(') == w[:idx].count(')'):
            break
    u = w[:idx]
    v = w[idx:]
    if check(u): #u가 올바른 괄호 문자열이면
        answer = u + solution(v) 
    else: #아니라면
        answer += '(' #4-1
        answer += solution(v) #4-2
        answer += ')'#4-3
        u = u[1:-1]
        # for i in range(len(u)): #4-4
        #     if u[i] == '(':
        #         u[i] = ')'
        #     else:
        #         u[i] = '(' 
        #문자열은 이렇게 수정 불가능!
        temp_u = ''
        for i in range(len(u)): #4-4
            if u[i] == '(':
                temp_u += ')'
            else:
                temp_u += '(' 

        answer += temp_u

    return answer

print(solution(p))