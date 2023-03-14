n = input()
n = int(n)
data = list(map(int, input().split()))

#code

data.sort(reverse = True)

count = 0
while len(data) != 0:
    for i in range(data[0]-1) :
        data.pop()
    del data[0]
    count += 1

print(count)

