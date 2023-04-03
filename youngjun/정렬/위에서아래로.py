def solution():
    N = int(input())
    nums = []
    for _ in range(N):
        nums.append(str(input()))
    nums.sort(reverse=True)

    answer = ' '.join(nums)
    
    print(answer)
solution()