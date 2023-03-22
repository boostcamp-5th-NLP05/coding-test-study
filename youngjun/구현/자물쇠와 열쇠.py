import copy
def solution(key, lock):
    answer = False
    M = len(key)
    N = len(lock)
    count_key, count_lock = 0, 0
    
    #n 만큼 패딩
    #회전 및 확인 * 4
    
    
    #N만큼 패딩
    new_lock = [[0] * (N + (2*M)) for _ in range((N + (2*M)))]
    for i in range(N):
        for j in range(N):
            new_lock[i+M][j+M] = lock[i][j]

    #회전 당 확인 총 4번
    for _ in range(4):
        #열쇠 회전
        rotation_key = [[0] * M for _ in range(M)]
        for i in range(M):
            for j in range(M):
                rotation_key[j][i] = key[M-i-1][j]
        key = rotation_key.copy()
        
        #확인 할 자물쇠
        #copy()를 쓰면 안되고 deepcopy를 쓰면 되는데 이유는 잘 모르겠음
        new_lock_copy = copy.deepcopy(new_lock)
        
        #한칸씩 이동하면서 더하기, 이동할때마다 new_lock_copy 초기화
        for i in range(M+N+1):
            for j in range(M+N+1):
                for k in range(M):
                    for l in range(M):
                        new_lock_copy[i+k][j+l] += key[k][l]
                cnt = 0
                
                #원래 자물쇠 부분이 다 1이라면 True 리턴
                for k in range(N):
                    for l in range(N):
                        if new_lock_copy[k+M][l+M] == 1:
                            cnt += 1
                        if cnt == N*N:
                            return True
                
                #다 1이 아니면 초기화하고 반복
                new_lock_copy = copy.deepcopy(new_lock)
                
    return False

#한시간 넘게걸림...