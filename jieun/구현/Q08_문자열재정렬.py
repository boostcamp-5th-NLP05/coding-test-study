import string
input_str = input()

letters = [] # 입력에서 알파벳 대문자만 저장할 리스트
num = 0 # 입력 중 숫자를 더한 값을 저장
for c in input_str:
    if c in string.ascii_uppercase:
        # 알파벳 대문자이면 letters에 넣기
       letters.append(c)
    else:
        # 숫자이면 num에 더하기
        num += int(c) 

letters.sort() # 오름차순 정렬
ans = "".join(letters) + str(num) # 정렬된 알파벳 대문자 뒤에 숫자 합 이은 문자열
print(ans)