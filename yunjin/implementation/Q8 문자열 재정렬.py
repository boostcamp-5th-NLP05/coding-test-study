word = input()

digit_sum = 0

new_word = []

for i in range(len(word)):

    # 숫자 합산하기
    if word[i].isdigit():
        digit_sum += int(word[i])
    else:
        new_word.append(word[i])

new_word.sort()

answer = ''.join(new_word) + str(digit_sum)
print(answer)