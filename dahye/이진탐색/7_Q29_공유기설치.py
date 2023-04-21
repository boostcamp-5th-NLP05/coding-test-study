def binary_search(data, C): 
    start = 0
    end = data[-1]-data[0]
    dis = 0 #최소 거리의 최대 거리
    #temp = [data[0], data[-1]] #공유기가 설치된 집 lsit
    while start <= end:
        count = 1
        mid = (start + end) // 2 #공유기 사이의 거리
        temp = data[0]

        for i in data:
            if temp + mid <= i:
                count+=1
                temp = i
            
        if count >= C: #공유기 설치 완료 or 더 많이 설치 -> 간격 늘리기
            start = mid+1
            dis = mid
        else: # 공유기 설치 더 해야함 -> 간격 줄이기
            end = mid - 1

    return dis

data = []
N, C = map(int,input().split())
for _ in range(N):
    data.append(int(input()))

data.sort()
print(binary_search(data, C))