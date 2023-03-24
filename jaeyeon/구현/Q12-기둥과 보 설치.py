def is_deleteable(build_map, c, r, a):
    if a == 0: # 기둥
        # 기둥 위에 기둥이 지어져있는 경우
        if build_map[r+1][c] == 6:
            return False
        
        # 위 아래에 보가 있는 경우
        if build_map[r][c] == 1 and build_map[r+1][c] == 1:
            return False
        
    else: # 보
        # 보 3개가 연달아 있을 때 중간의 보를 뺄 순 없다
        if build_map[r][c] == 2:
            # 보의 오른쪽도 겹쳐져 있을 때
            if build_map[r][c+1] == 2:
                if build_map[r][c+2] == 2:
                    return False
                
            # 보의 왼쪽도 겹쳐져 있을 때
            if build_map[r][c-1] == 2:
                if build_map[r][c-2] == 2:
                    return False
        
        # 보 위에 기둥이 지어져 있는 경우
        if (build_map[r][c] == 4 and build_map[r+1][c] >= 3) or (build_map[r][c+1] == 4 and build_map[r+1][c] >= 3):
            return False
            
    return True

def solution(n, build_frame):
    answer = []
    # a - 0: 기둥, 1: 보
    # b - 0: 삭제, 1: 설치
    # 기둥 3, 보 1 => 1: 보, 2: 보 2개, 3: 기둥, 4 : 기둥, 보, 6 : 기둥 2개
    
    build_map = [[0 for _ in range(n+1)] for _ in range(n+1)]
    structs = []            # 현재 구조물들을 저장할 배열
    for frame in build_frame:
        c, r, a, b = frame
        if a == 0:          # 기둥
            if b == 0:      # 삭제        
                if is_deleteable(build_map, c, r, a):
                    del structs[structs.index([c, r, a])]
                    build_map[r][c] -= 3
                    build_map[r+1][c] -= 3
                    
            else:           # 설치
                if (r == 0 and build_map[r][c] == 0) or build_map[r][c] in [1, 3, 4, 5]:
                    build_map[r][c] += 3
                    build_map[r+1][c] += 3
                    structs.append([c, r, a])
        else:               # 보
            if b == 0:      # 삭제
                if is_deleteable(build_map, c, r, a):
                    del structs[structs.index([c, r, a])]
                    build_map[r][c] -= 1
                    build_map[r][c+1] -= 1
                    
            else:           # 설치
                if build_map[r][c] in [3,4] or build_map[r][c+1] in [3,4] or (build_map[r][c] == 1 and build_map[r][c+1] == 1) :
                    build_map[r][c] += 1
                    build_map[r][c+1] += 1
                    structs.append([c, r, a])
    
    structs.sort()
    answer = structs
    
    return answer
if __name__=="__main__":
    n = 5
    build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
    print(solution(n, build_frame))
