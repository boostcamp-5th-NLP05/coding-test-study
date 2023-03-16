# O(N^2) 풀이
def solution_O_N2(food_times, k):
    answer = 0
    if sum(food_times) < k:         # k초 안에 모든 음식을 먹을 수 있으므로 -1을 반환
        return -1

    N = len(food_times)
    time_list = []
    idx = 0
    cnt = 0
    while True:
        if food_times[idx] == 0:
            idx = (idx + 1) % N
            continue

        time_list.append(idx + 1)   # time_list에는 음식이 먹는 순서대로 append
        cnt += 1
        food_times[idx] -= 1
        idx = (idx + 1) % N
        if cnt > k:
            break

    answer = time_list[k]           # 전체 순서 중 k번째로 먹는 음식
    return answer

# O(N) 풀이
def solution_O_N(food_times, k):
    answer = 0
    if sum(food_times) < k: return -1
    
    N = len(food_times)
    step = k // N
    index = k % N
    
    if step == 0:
        answer = (index + 1) % N
        
    else:
        left_list = []
        for idx, food_time in enumerate(food_times):
            left_list.append([idx, food_time])
            
        while step != 0:
            index_add = 0
            left_list_tmp = []
            for idx in range(N):
                # 모든 요소에서 step만큼 빼기
                left_list[idx][1] -= step
                
                # 추가로 진행해야 할 index 계산
                if left_list[idx][1] <= 0:
                    index_add -= left_list[idx][1]
                else:
                    left_list_tmp.append([idx, left_list[idx][1]])
            
            # 새로운 left_list와 N 생성        
            left_list = left_list_tmp.copy()
            N = len(left_list)
            
            index += index_add

            # 새로운 step과 index 계산
            step = index // N
            index = index % N
        
        answer = left_list[index][0] + 1
        
    return answer