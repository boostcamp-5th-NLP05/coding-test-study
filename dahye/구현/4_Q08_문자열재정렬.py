data = list(map(str, input())) #데이터를 하나하나씩 list에 저장

#code
data.sort() # 숫자 -> 문자로 정렬
result = 0  # 숫자 데이터를 모두 더한 값을 저장하기 위한 변수
while True :
    if data[0] in "1234567890": #숫자이면
        result+=int(data.pop(0)) #더해주면서 제외
    else: #문자이면
        break #반복문 탈출
print(''.join(data) + str(result))
