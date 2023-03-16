n = input()
n = int(n)
data = list(map(int, input().split()))

#code

data.sort()

#몇 명의 모험가는 마을에 그대로 남아 있어도 되는 조건을 고려하지 못함

temp = [] #임의의 한 그룹
result = 0 # 총 그룹 수

for i in data:
    temp.append(i)

    if max(temp) <= len(temp):
        result += 1
        temp = []

print(result)

