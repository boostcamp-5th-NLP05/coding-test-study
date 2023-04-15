class Solution:
    def isUgly(self, n: int) -> bool:

        flag = False
        cnt = 1

        if n == 0:
            return False


        # 2, 3, 5 로 나눠진 경우가 한번 이상 있어야 반복분 진입함.
        while cnt != 0:
            cnt = 0

            if n % 2 == 0:
                n /= 2
                cnt += 1
            elif n % 3 == 0:
                n /= 3
                cnt += 1
            elif n % 5 == 0:
                n /= 5
                cnt += 1

            # 2, 3, 5 나누기를 반복하다가 1이 되는 경우가 존재 했다면 해당 수는 못생긴 수
            if n == 1:
                flag = True
                break

        return flag