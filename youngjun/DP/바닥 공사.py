n = int(input())
d = [0] * 1000
d[0] = 1
d[1] = 3

for i in range(2,n):
    d[i] = ((d[i-2] * 2) + d[i-1]) % 796796

print(d[n-1])