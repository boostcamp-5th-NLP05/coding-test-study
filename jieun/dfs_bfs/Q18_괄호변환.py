def is_right(u):
    # u가 올바른 문자열인지 반환한다.
    stack = []
    for ch in u:
        if ch == "(":
            stack.append(ch)
        elif len(stack) == 0:
            # ")"와 쌍을 이룰 "("가 없다
            return False
        else:
            stack.pop()
    if len(stack) == 0:
        # "()" 모두 쌍을 이룬다.
        return True
    else:
        # "("만 남아있다.
        return False


def find_(s):
    if s == "":  # 빈 문자열 반환
        return ""
    
    left = 0 # "(" 개수
    right = 0 # ")" 개수
    # left == right 일 때의 idx를 구한다.
    for idx, ch in enumerate(s):
        if ch == "(":
            left += 1
        else:
            right += 1
        if left == right:
            break
    
    # u,v 찾기
    u = s[: idx + 1]
    v = s[idx + 1 :] if idx + 1 < len(s) else ""

    res_list = []
    if is_right(u): 
        # u가 올바른 문자열이면 u + v에 1단계
        res_list = [u, find_(v)]
    else:
        # u가 올바른 문자열이 아니면
        # ( + {v에 1단계} + ) + {u의 첫 번째와 마지막 문자 제거한 문자열의 반대 괄호}
        res_list = ["(", find_(v), ")"]
        for ch in u[1 : len(u) - 1]:
            if ch == "(":
                res_list.append(")")
            else:
                res_list.append("(")
                
    return "".join(res_list) # res_list에 있는 문자들을 붙여 문자열로 만든다.


def solution(p):
    answer = find_(p)
    return answer
