from itertools import combinations
import copy

def make_transpose(n,data): #전치행렬 만드는 함수
    trans = []
    for i in range(n):
        col = []
        for j in data:
            col.append(j[i])
        trans.append(col)
    return trans

def is_avoid(n,data): #감시 피하는지 반환하는 함수
    for i in data:
        before = -1                     #행에서 X가 아닌 것 저장 
        if 'S' in i and 'T' in i:
            for j in i:
                if j == 'T':            #지금 보고있는것과 before가 [T,S] [S,T] 이런 식이면 False 반환
                    if before == 'S':
                        return False
                if j == 'S':
                    if before == 'T':
                        return False
                if j != 'X':            #행에서 X가 아닌 것 저장 
                    before = j
                    
    data = make_transpose(n,data)       #전치해서 다시 확인
    
    for i in data:
        before = -1
        if 'S' in i and 'T' in i:
            for j in i:
                if j == 'T':
                    if before == 'S':
                        return False
                if j == 'S':
                    if before == 'T':
                        return False
                if j != 'X':
                    before = j
    return True

def solution():
    n= int(input())
    data = []
    for _ in range(n):
        data.append(list(map(str, input().split())))
    
    
    info_X = [] 

    for r in range(n):
        for c in range(n):
            if data[r][c] == 'X':  
                info_X.append([r,c])  #X인 좌표 저장

    answer = []
    comb = list(combinations(info_X, 3)) #X 좌표 3개 조합
    
    for i in comb: #각 조합별로 진행
        copy_data = copy.deepcopy(data) 
        copy_data[i[0][0]][i[0][1]] = 'O' #벽 세우기
        copy_data[i[1][0]][i[1][1]] = 'O'
        copy_data[i[2][0]][i[2][1]] = 'O'
        
        if is_avoid(n,copy_data): #각 조합마다 확인해서 피할 수 있는 경우가 있으면 바로 리턴
            return print('YES')
        else:
            continue
    
    return print('NO')

solution()