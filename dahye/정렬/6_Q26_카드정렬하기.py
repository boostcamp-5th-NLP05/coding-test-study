N = int(input())
data = []
for i in range(N):
    data.append(int(input()))
data.sort() #작은 수부터 묶어야함
sum_list = [] # j번째 합치기에서 비교 수 저장 list
s = data[0] # j번째 합치기에서 비교 수
for j in range(1, N):
    s += data[j]
    sum_list.append(s)
print(sum(sum_list)) #총 합치기 수 



