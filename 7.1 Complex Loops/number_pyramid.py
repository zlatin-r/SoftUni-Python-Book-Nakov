n = int(input())
num = 1

for row in range(1, n + 1):
    for col in range(1, row + 1):
        print(num, end=" ")
        num += 1
        if col >= row:
            print()
        if num > n:
            break
    if num > n:
        break
