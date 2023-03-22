import numpy as np

def rotation(data): #90도 회전함수
    new_data = [[0 for _ in range(len(data))] for _ in range(len(data))]
    for x in range(len(data)):
        for y in range(len(data)):
            new_data[y][len(data)-x-1] = data[x][y]
    return new_data

def check(key, lock , new_lock, j, k, m): #열 수 있는지 여부를 알아내는 함수
    new_lock_temp = new_lock.copy()
    for i in range(len(key)):
        for w in range(len(key)):
            new_lock_temp[j+i,k+w] = key[i][w] + lock[i][w] 
    print(new_lock_temp[m-1:len(new_lock)-m+1,m-1:len(new_lock)-m+1])
    print('-------------')
    print(np.array([[1 for _ in range(len(new_lock)-2*(m-1))] for _ in range(len(new_lock)-2*(m-1))]))
    if np.array_equal(new_lock_temp[m-1:m-1,len(new_lock)-m+1:len(new_lock)-m+1], np.array([[1 for _ in range(len(new_lock)-2*(m-1))] for _ in range(len(new_lock)-2*(m-1))])):
        return True
    return False

def solution(key, lock):
    answer = True
    #Lock padding
    new_lock1 = []
    for temp_lock in lock:
        new_lock1.append([0]*(len(key)-1) + temp_lock + [0]*(len(key)-1))
    new_n = len(new_lock1[0])
    for n in range(len(key)-1):
        new_lock1.insert(n, [0]*(new_n))
        new_lock1.append([0]*(new_n))
    m = len(key)
    new_lock = np.array(new_lock1) #numpy로 정사각형의 slicing 가능
    for i in range(4):
        for j in range(len(new_lock)-m+1): #오른쪽, 아래쪽으로 한칸씩 이동하면서 check
            for k in range(len(new_lock)-m+1):
                print(check(key, new_lock[j:j+m,k:k+m], new_lock, j,k , m))
                if check(key, new_lock[j:j+m,k:k+m], new_lock, j,k , m) == True:
                    
                    return answer
        key = rotation(key)
                      
    answer = False
    return answer
key = input()
lock = input()
print(solution(key,lock))