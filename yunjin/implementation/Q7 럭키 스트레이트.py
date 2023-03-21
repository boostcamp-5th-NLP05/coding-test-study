number = input()
number = list(map(int, number))

# 왼쪽 합 , 오른쪽 합
left_sum = sum(number[:int(len(number)/2)])
right_sum = sum(number) - left_sum

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")