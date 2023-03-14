if __name__ == "__main__":
    line = input()
    numbers = [int(c) for c in line]
    answer = numbers.pop(0)
    for n in numbers:
        if answer * n == 0 or answer == 1 or n == 1:
            answer += n
        else:
            answer *= n

    print(answer)
