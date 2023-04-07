from itertools import permutations

def solution(n, weak, dist):
    for i in range(len(weak)): #원형이므로 일자로 펴준다
        weak.append(weak[i] + n)
    total_friends = list(permutations(dist, len(dist))) #친구 조합 생성
    result = len(dist) + 1 #최대 친구 수 -1반환을 위해
    for start_weak in range(len(weak)):
        for friends in total_friends:
            count = 1 #친구 수
            position = weak[start_weak] + friends[count-1] #친구의 마지막 위치
            for idx in range(start_weak, start_weak + len(weak)): #취약지점 탐색

                # 마지막까지 탐색된 위치보다 현재 취약 지점의 값이 크다면
                if (weak[idx] > position):
                    # 친구 추가
                    count +=1
                    # 친구들을 더 이상 투입할 수 없을 경우
                    if (count > len(dist)):
                        break
                    # 마지막까지 확인된 위치를 업데이트
                    position = weak[idx] + friends[count-1]

            # 투입된 친구의 최소값을 계산
            result = min(result, count)
    if (result > len(dist)): #점검 불가
        return -1

    return result