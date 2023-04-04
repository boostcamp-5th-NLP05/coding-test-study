n = int(input())
data = list(map(int,input().split()))
median = n//2 if n % 2 == 0 else n//2 + 1
data.sort()
print(data[median-1])