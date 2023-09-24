number = int(input())

first = number // 100
second = number % 100 // 10
third = number % 10
N = first + second
M = first + third

for row in range(N):
    for col in range(M):
        if number % 5 == 0:
            number -= first
        elif number % 3 == 0:
            number -= second
        else:
            number += third

        print(number, end=" ")
    print()
