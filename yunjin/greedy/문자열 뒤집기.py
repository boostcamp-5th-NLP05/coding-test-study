N = input()
strings = list(map(str, N))

answer = 0

for i in range(len(strings)-1):
    # 바뀌는 경우를 모두 카운트 해준다.
    if strings[i] != strings[i + 1]:
        answer += 1


# 짝수번 바뀌었다면 절반이 최솟값.
if answer % 2 == 0:
    print(int(answer/2))

# 홀수번 바뀌었다면 strings 가 짝수 분할 된 것 : answer=3 이면 4개 영역으로 분할 된 것 -> (3+1)/2 = 2 번만 바꾸면된다.
else:
    print(int(answer//2)+1)
