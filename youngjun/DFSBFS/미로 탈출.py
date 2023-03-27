def solution():
    n, m = map(int,input().split())
    map_ = []
    
    for i in range(n):
        map_.append(list(map(int, input())))
    
    c_move = [1, 0, -1, 0]
    r_move = [0, 1, 0, -1]
    visited = [[0,0,1]]
    
    while visited:
        c,r,cnt = visited.pop(0)
        for i in range(4):
            nc = c + c_move[i]
            nr = r + r_move[i]
            if nc >= 0 and nc < m and nr >= 0 and nr < n:
                if map_[nr][nc] == 1 or map_[nr][nc] > cnt + 1:
                    map_[nr][nc] = cnt + 1
                    if nr == n-1 and nc == m-1:
                        answer = cnt + 1
                        return answer
                    visited.append([nc,nr,cnt + 1])
    
    return -1

solution()