def solution(p):

    def MakeTwoWords(word): #단어 두개로 만드는 함수
        count_left = 0
        count_right = 0
        word1,word2 = '',''
        for i in range(len(word)):
            if word[i] == '(':
                count_left+=1
            else:
                count_right+=1

            if count_left == count_right:
                word1 = word[:i+1]
                word2 = word[i+1:]
                break

        return word1,word2
        
    def IsWrong(word): #올바른 괄호 확인 함수
        count_left = 0
        count_right = 0
        wrong = False
        for i in word:
            if i == '(':
                count_left+=1
            else:
                count_right+=1
            if count_right > count_left:
                wrong = True
                break
        return wrong

    def main(word): #재귀 돌릴 함수
        answer = ''
        if word == '': #1.빈 문자열 반환
            return ''
        
        if not IsWrong(word): #이미 올바른 괄호면 반환
            return word
        
        u=''
        v=''
        u,v = MakeTwoWords(word) #2.두 "균형잡힌 괄호 문자열" u, v로 분리
        
        if not IsWrong(u):       #3.올바른 괄호면 v로 재귀
            answer += u
            answer += main(v)    #3.1

        if IsWrong(u):           #4.올바른 괄호가 아닐 때
            a = ''
            a += '('             #4.1
            a += main(v)         #4.2
            a += ')'             #4.3
            for i in u[1:-1]:   #4.4
                if i == '(':
                    a += ')'
                else:
                    a += '('
            return a            #4.5

        return answer

                
    return main(p)