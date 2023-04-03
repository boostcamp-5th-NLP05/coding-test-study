def solution():
    N = int(input())
    nums = []
    for _ in range(N):
        nums.append(int(input()))
    
    nums.sort(reverse=True)

    for i in nums:
        print(i, end = ' ')

solution()