from collections import deque

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        if word1 == word2:
            return 0

        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))

        w1 = list(word1)
        w2 = list(word2)

        num = 0
        queue = deque()
        queue.append((0, 0))
        visited = set()

        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()

                # 같다면 아무런 편집도 하지 않고 인덱스 증가
                while i < len(w1) and j < len(w2) and w1[i] == w2[j]:
                    i += 1
                    j += 1

                # BFS 이므로 가장 먼저 도달한 경우가 최소 편집 거리 이다.
                if i == len(w1) and j == len(w2):
                    return num

                # BFS 에 대한 각각의 경우의 수를 queue 에 추가
                if (i, j) not in visited:
                    visited.add((i, j))
                    queue.append((i, j + 1)) # w1 의 i 번째 문자를 삭제 하는 경우
                    queue.append((i + 1, j + 1)) # w1 의 i 번째 문자를 w2 의 j 번째 문자로 교체 하는 경우
                    queue.append((i + 1, j)) # w1 의 i 번째 문자를 w2 의 j 번째 문자로 추가 하는 경우

            num += 1
