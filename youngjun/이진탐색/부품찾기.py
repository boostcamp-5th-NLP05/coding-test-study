def binary_search(array,target,start,end):
    while start<= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 'yes'
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 'no'

n = int(input())
gage = list(map(int,input().split()))
m = int(input())
son = list(map(int,input().split()))

gage.sort()

answer = []
for i in son:
    answer.append(binary_search(gage,i,0,len(gage)))
    
print(' '.join(answer))