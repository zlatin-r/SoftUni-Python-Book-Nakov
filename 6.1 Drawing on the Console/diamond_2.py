n = int(input())

left_right = (n - 1) // 2

for row in range(0, (n + 1) // 2):
    mid = n - 2 * left_right - 2
    print("-" * left_right, end="")
    print("*", end="")

    if mid < 0:
        print("-" * left_right)
    else:
        print("-" * mid, end="")
        print("*", end="")
        print("-" * left_right)
    left_right -= 1
left_right = 0

for row in range((n - 1) // 2):
    left_right += 1
    print("-" * left_right, end="")
    print("*", end="")

    mid = n - 2 * left_right - 2

    if mid >= 0:
        print("-" * mid, end="")
        print("*", end="")
    print("-" * left_right)