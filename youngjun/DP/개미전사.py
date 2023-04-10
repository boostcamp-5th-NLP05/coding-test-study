d = [0]* 101
n = int(input())
food_save = list(map(int,input().split()))

d[0] = food_save[0]
d[1] = max(food_save[0],food_save[1])

for i in range(2,n):
    d[i] = max(d[i-1],d[i-2]+food_save[i])
    
print(d[n-1])