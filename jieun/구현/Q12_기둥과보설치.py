def solution(n, build_frame):
    answer = []
    # 0: 빈 곳, 1: 보, 10: 기둥, 11: 기둥+보
    # 패딩 0 1 ... n-1 n   패딩 -> 문제 좌표
    # 0    1 2 ... n   n+1 n+2 -> 패딩 고려한 좌표
    map_ = [[0 for _ in range(n+3)] for _ in range(n+3)]  # 교차점 -> 칸, padding
    for i in range(n+3):  # 패딩
        map_[i][0] = -1
        map_[i][n+2] = -1
        map_[0][i] = -1
        map_[n+2][i] = -1

    def is_ok(x, y, obj):
        # (x,y) 에 obj를 설치할 수 있는지 조건 확인.
        # 단, (x,y)에 obj 없을 때는 무시(return True)
        
        # if map_[x][y] < 1: return True # 확인하려는 위치가 패딩(-1)이거나 아무것도 없을 때(0) 무시 --> 틀림: obj가 아닐 때도 무시해야 함.
        
        if obj == 0:  # 기둥 조건 확인
            if map_[x][y] // 10 != 1:
                return True  # 기둥 아님 (무시)
            if y == 1:
                return True  # 바닥 위에 있다
            if map_[x-1][y] % 10 == 1:
                return True  # 보의 오른쪽 끝 위에 있다.
            if map_[x][y-1] // 10 == 1:
                return True  # 아래에 기둥 존재
            if map_[x][y] % 10 == 1:
                return True  # 보의 왼쪽 끝 위에 있다.
        else:  # 보 조건 확인
            if map_[x][y] % 10 != 1:
                return True  # 보 아님 (무시)
            if map_[x][y-1] // 10 == 1:
                return True  # 왼쪽 끝이 기둥 위에 있다
            if map_[x+1][y-1] // 10 == 1:
                return True  # 오른쪽 끝이 기둥 위에 있다
            if map_[x-1][y] % 10 == 1 and map_[x+1][y] % 10 == 1:
                return True  # 두 보 사이에 있다
        return False

    for x, y, a, b in build_frame:
        x += 1  # 입력 -> 패딩 적용한 값
        y += 1

        if a == 0:  # 기둥
            if b == 0:  # 삭제
                map_[x][y] -= 10
                if not is_ok(x-1, y+1, 1) or not is_ok(x, y+1, 1) or not is_ok(x, y+1, 0):
                    map_[x][y] += 10  # 원상 복구 (삭제 무시)
            else:  # 설치
                map_[x][y] += 10
                if not is_ok(x, y, a):
                    map_[x][y] -= 10 # 원상 복구 (설치 무시)
        else:  # 보
            if b == 0:  # 삭제
                map_[x][y] -= 1
                if (not is_ok(x-1, y, 1)) or (not is_ok(x+1, y, 1)) or (not is_ok(x, y, 0)) or (not is_ok(x+1, y, 0)):
                    map_[x][y] += 1  # 원상 복구 (삭제 무시)
            else:  # 설치
                map_[x][y] += 1
                if not is_ok(x, y, a):
                    map_[x][y] -= 1 # 원상 복구 (설치 무시)

    # 문제에 주어진 순서대로 추가한다
    for x in range(1, n+2):
        for y in range(1, n+2):
            if map_[x][y] // 10 == 1:  # 기둥
                answer.append([x-1, y-1, 0])  # 패딩 적용한 좌표 -> 문제 좌표
            if map_[x][y] % 10 == 1:  # 보
                answer.append([x-1, y-1, 1])

    return answer
