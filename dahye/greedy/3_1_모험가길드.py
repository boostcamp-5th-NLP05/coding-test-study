n = input()
n = int(n)
data = list(map(int, input().split()))

#code

data.sort()
count = 0 # 총 그룹 수
temp = [] # 임의의 그룹
# 몇 명의 모험가는 마을에 그대로 남아 있어도 된다는 조건을 고려하여 다시작성
for i in data:
    temp.append(i)
    if len(temp)>=max(temp):
        temp = []
        count += 1

print(count)

