n = int(input())
guild = list(map(int, input().split()))
guild.sort()

answer = 0
cnt = 0

for i in range(len(guild)):
    
    cnt += 1
    
    if guild[i] == cnt:
        answer += 1
        cnt = 0
    
    if guild[i] > len(guild) - i:
        break

print(answer)