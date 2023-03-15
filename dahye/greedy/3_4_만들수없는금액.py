n = int(input())
data = list(map(int, input().split()))

#code

data.sort()
temp = 1
for i in data:
    if i > temp:
        break
    else:
        temp += i
print(temp)