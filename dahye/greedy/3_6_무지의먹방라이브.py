food_times = list(map(int, input().split()))
k = int(input())

#code

temp = 0
for i in range(k):
    if food_times[temp] == 0: #음식이 없으면
        temp += 1 #다음 음식 먹기
        if temp == len(food_times): #다음 음식이 마지막 음식이었다면 다시 처음 음식으로
            temp = 0
    food_times[temp] -= 1 #1 초씩 먹기
    temp += 1
    if temp == len(food_times):
        temp = 0
print(temp+1)