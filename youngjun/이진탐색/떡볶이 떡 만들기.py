n,m = map(int,input().split())
rice = list(map(int,input().split()))

def binary_search(array,target,start,end):
    while start<= end:
        mid = (start + end) // 2
        tmp = 0
        
        for i in array:
            if i - mid > 0:
                tmp += i - mid

        if tmp > target: #
            start = mid + 1
        else:
            end = mid - 1

    return mid

print(binary_search(rice,m,0,max(rice)))
