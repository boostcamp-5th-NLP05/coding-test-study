def solution(p):
    answer = ''

    # 균형잡힌 괄호 문자열 확인
    def separate_u_v(p):  # 문자열 p를 u와 v로 분리
        # u : 균형잡힌 괄호 문자열, v : 나머지
        open_p, close_p = 0, 0
        for i in range(len(p)):
            if p[i] == '(':
                open_p += 1
            else:
                close_p += 1
            if open_p == close_p:
                return p[:i + 1], p[i + 1:]  # u, v

    # 올바른 괄호 문자열 확인
    def is_correct_string(input_string):
        stack = []
        idx = 0

        # 반복문을 통해 짝이 맞는 것을 삭제해준다.
        while True:
            if not stack:
                stack.append(input_string[idx])
            else:
                if stack[-1] == "(" and input_string[idx] == ")":
                    stack.pop() # 조합이 맞다면 제거
                else:
                    stack.append(input_string[idx]) # 짝이 안 맞으므로 쌓아준다.

            idx += 1
            if idx >= len(input_string):
                break

        # 반복문 탈출 시 stack 에 남아 있는게 있다면 올바른 괄호 문자열이 아님.
        if stack:
            return False
        else:
            return True

    # 뒤집기
    def get_reverse_string(strings):
        reverse_dict = {"(": ")", ")": "("}
        result = ''
        for string in strings:
            result += reverse_dict[string]
        return result

    def make_correct_string(s):

        if s == '':
            return ''

        u, v = separate_u_v(s)  # 과정 2

        if is_correct_string(u):
            return u + make_correct_string(v)
        else:
            r = "("
            r += make_correct_string(v)
            r += ")"
            r += get_reverse_string(u[1:-1])
            return r

    answer = make_correct_string(p)
    return answer
