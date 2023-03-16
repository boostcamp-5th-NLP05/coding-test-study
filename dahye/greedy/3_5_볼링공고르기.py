import math
n, m = input().split()
n = int(n)
m = int(m)
data = list(map(int, input().split()))

#code

data.sort()
temp_list = [0]
temp = data[0] #공의 무게가 같은것이 몇개있는지 구하기
k = 0
for i in range(n):
    if temp == data[i]:
        temp_list[k] += 1
    else:
        k+=1
        temp_list.append(1)
        temp = data[i]

result = math.factorial(n)/math.factorial(n-2)/2 #전체 조합
for i in temp_list: #공의 무게가 같은 조합을 빼기
    if i != 1 :
        result -= math.factorial(i)/math.factorial(i-2)/2

print(int(result))