def solution(s):
    answer_list = [] #각 candi들 마다 구한 표현의 총 길이 list
    for candi in range(1, len(s)//2+1): #1부터 총길이의 절반값까지 확인
        temp = s[0:candi] # 반복 수를 확인해야 할 첫번째 문자열을 반복 여부 확인 변수 temp에 저장
        count = 0 #반복 수
        result = '' # 각 candi의 최종 표현 string
        for j in range(len(s)//candi+1):
            if temp == s[candi*j:candi*(j+1)]: #반복이 맞으면 1 추가
                count += 1
            else: #반복이 아니면 result에 추가하고 temp를 바꾸고 count 리셋
                if count == 1: #count가 1이면 숫자 없이 추가
                    result = result + temp
                else: #count가 1이 아니면 숫자와 함께 추가
                    result = result + str(count) + temp
                temp = s[candi*j:candi*(j+1)]
                count = 1
        
        if len(s)%candi !=0: #candi보다 적은 수 만큼 s가 남았을 때 == 0으로 나누어떨어지지 않을 때
            result += s[candi*j:candi*(j+1)] #따로 뒤에 붙임
        answer_list.append(len(result))
        
    answer_list.append(len(s)) #반복이 없을 때 추가     
    answer = min(answer_list)
    return answer

s = input()
print(solution(s))