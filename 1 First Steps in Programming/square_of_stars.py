n = int(input())

for num in range(0, n):
    print("*", end="")

print("")

for num in range(0, n - 2):

    print("*", end="")
    for num in range(0, n - 2):
        print(" ", end="")
    print("*", end="")

    print("")

for num in range(0, n):
    print("*", end="")
