N = int(input())
arr = []
for _ in range(N):
    name, score = input().split()
    arr.append((name, int(score)))

arr.sort(key=lambda x: x[1])
sorted_name = [a[0] for a in arr]

print(sorted_name)
    
    