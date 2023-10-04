n = int(input())
num_rows = n

print("%" * (2 * n))

if n % 2 == 0:
    num_rows -= 1

for i in range(0, num_rows):

    print("%", end="")

    if i == num_rows // 2:
        print((" " * (n - 2)) + "**" + (" " * (n - 2)) + "%")
    else:
        print(" " * (n * 2 - 2) + "%")

    print(end="")

print("%" * (2 * n))
