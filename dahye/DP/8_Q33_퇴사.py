N = int(input())
money = [] #받을 수 있는 금액
term = [] #상담기간
for _ in range(N):
    a, b = map(int,input().split())
    money.append(b)
    term.append(a)

d = money.copy() #d는 i번째 날까지 받을 수 있는 금액의 최대 값

for i in range(N):
    for j in range(i):
        before = i-j-term[j] #term만큼의 이전의 날에서 더해줌
        if before >=0 and before <N:
            d[i] = max(d[j]+money[i], d[i])
        if N-i < term[i]: #상담을 퇴사전까지 할 수 없을 때
            d[i] = d[i-1]
if N == 1 and term[0] > 1:
    print(0)
else:   
    print(max(d))
#90퍼쯤에 오답처리....