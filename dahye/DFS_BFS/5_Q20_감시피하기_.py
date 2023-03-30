from itertools import combinations
import copy

n = int(input())
data = []
teacher = []
for i in range(n):
    temp_list = list(input().split())
    data.append(temp_list)
    for j in range(n):
        if temp_list[j] == 'T':
            teacher.append([i,j])

#code
#선생님이 학생을 만나는지 탐지함수 생성
def check(x,y,data,n) : #선생님의 위치 입력받음
    i=1
    while True : #모두 끝까지 도달했을 때
        nx1 = x+i #오른쪽 탐색
        nx2 = x-i #왼쪽 탐색
        ny1 = y+i #위쪽 탐색
        ny2 = y-i #아래쪽 탐색
        if nx1 >= n: #범위 초과하면 마지막 범위로 되돌려서 판단 while문 조건 때문
            nx1 = n-1
        if nx2 <= -1: 
            nx2 = 0
        if ny1 >= n: 
            ny1 = n-1
        if ny2 <= -1: 
            ny2 = 0

        if data[nx1][y] == 'S' or data[nx2][y] == 'S' or data[x][ny1] == 'S' or data[x][ny2] == 'S': #학생이 있으면
                return True #감시로부터 피할 수 없음
        else:
            i+=1   
        if data[nx1][y] == 'O': #장애물 마주치면 더이상 볼 필요 없으므로 해당방향의 맨 뒤로 이동
            nx1 == n-1
        if data[nx2][y] == 'O':
            nx2 == 0
        if data[x][ny1] == 'O':
            ny1 == n-1 
        if data[x][ny2] == 'O':
            ny2 == 0           
        if nx1 == n-1 and nx2 == 0 and ny1 == n-1 and ny2 == 0 : #모두 끝까지 도달했다면 break
            break
    return False

#이렇게 되면 S가 맨 끝에 있을때를 고려하지 못함 -> 다시작성

#장애물을 설치할 곳 후보
def solution(n,data,teacher) :
    o_list = []
    for oi in range(n):
        for oj in range(n):
            if data[oi][oj] == 'X':
                o_list.append([oi,oj])
    #3개의 장애물 조합 combination
    comb = list(combinations(o_list, 3))

    answer = False
    for com1, com2, com3 in comb:
        temp_data = copy.deepcopy(data)
        com1_1, com1_2 = com1
        com2_1, com2_2 = com2
        com3_1, com3_2 = com3
        temp_data[com1_1][com1_2] = 'O'
        temp_data[com2_1][com2_2] = 'O'
        temp_data[com3_1][com3_2] = 'O' #장애물 설치

        
        for i,j in teacher: #선생님 만나면 탐지 시작
            if check(i,j,temp_data,n) == True: #만난 선생님이 있다면
                return 'NO'


    return 'YES' #감시 안받음
print(solution(n,data,teacher))