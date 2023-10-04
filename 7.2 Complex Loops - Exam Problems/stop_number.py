n = int(input())
m = int(input())
s = int(input())
num = 0

for i in range(m, n - 1, - 1):
    if i % 2 == 0 and i % 3 == 0:
        num = i
        if num == s:
            break
        print(num, end=" ")
