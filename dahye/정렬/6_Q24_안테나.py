N = int(input())
data = list(map(int,input().split()))
data.sort()

if len(data)%2 == 0: #집이 짝수개일때
    temp1 = data[len(data)//2-1]
    temp2 = data[len(data)//2]
    sum1 = 0
    sum2 = 0 #가운데 두 집중 거리의 총합이 작은 집을 계산하여 출력
    for i in data:
        sum1 += abs(temp1-i)
        sum2 += abs(temp2-i)
    if sum1 > sum2 : #같으면 작은값을 출력하므로 조건을 다음과같이 줌
        print(temp2)
    else:
        print(temp1)
else: #집이 홀수개일때
    print(data[len(data)//2])

