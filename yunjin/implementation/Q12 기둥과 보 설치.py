def solution(n, build_frame):

    update_map = set()

    # 정상 맵인지 완전 탐색하는 함수
    def is_normal(update_map):

        for material in update_map:
            # 보 라면
            if material[2] == 1:
                # 한쪽에라도 기둥이 있으면 된다.
                if (material[0], material[1] - 1, 0) in update_map or \
                        (material[0] + 1, material[1] - 1, 0) in update_map:
                    continue
                # 양쪽에 보가 있으면 된다.
                if (material[0] - 1, material[1], 1) in update_map and \
                        (material[0] + 1, material[1], 1) in update_map:
                    continue

                return False

            # 기둥 이라면
            elif material[2] == 0:

                # 바닥이라면
                if material[1] == 0:
                    continue

                # 아래에 기둥이 있다면
                if (material[0], material[1] - 1, 0) in update_map:
                    continue

                # 양쪽에 보가 하나라도 있으면 된다.
                if (material[0] - 1, material[1], 1) in update_map or \
                        (material[0], material[1], 1) in update_map:
                    continue

                return False

        return True


    for frame in build_frame:

        # 추가한다면
        if frame[3] == 1:
            update_map.add((frame[0], frame[1], frame[2]))

            if not is_normal(update_map):
                update_map.remove((frame[0], frame[1], frame[2]))

        # 삭제한다면
        if frame[3] == 0:

            update_map.remove((frame[0], frame[1], frame[2]))

            if not is_normal(update_map):
                update_map.add((frame[0], frame[1], frame[2]))

    r = []
    for f in update_map:
        r.append(list(f))
    r.sort(key=lambda x: (x[0], x[1], x[2]))

    return r