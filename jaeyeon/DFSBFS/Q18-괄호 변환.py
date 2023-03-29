def check_right(sub):
    # 스택을 활용해서 괄호가 올바르게 되어있는지 확인
    stack = []
    for c in sub:
        if c == "(":
            stack.append(1)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


def check(w):
    # 올바른 괄호 문자열이면 바로 w 반환
    if check_right(w):
        return w

    # step 1 : 빈 문자열 반환
    if len(w) == 0:
        return ""

    # step 2 : w를 u, v로 분리
    u, v = "", ""
    for idx in range(2, len(w) + 1):
        sub = w[:idx]
        if sub.count("(") == sub.count(")"):
            u = sub
            v = w[idx:]
            break
    # step 3: u가 올바른 괄호 문자열일 때
    if check_right(u):
        # step 3-1: u에 v에 대해서 1단계부터 실행한 결과를 반환 
        return u + check(v)
    # step 4: u가 올바른 괄호 문자열이 아닐 때
    else:
        # step 4-1, 4-2, 4-3
        new_sub = "(" + check(v) + ")"

        # step 4-4: 앞 뒤 문자 제거하고 괄호 방향 뒤집기
        u = u[1:-1]
        u_list = list(u)
        for idx, val in enumerate(u_list):
            if val == "(":
                u_list[idx] = ")"
            else:
                u_list[idx] = "("
        u = "".join(u_list)
        new_sub += u

        # step 4-5: 생성된 문자열 반환
        return new_sub

def solution(p):
    answer = check(p)

    return answer


# 17분 24초
# 프로그래머스 정답
