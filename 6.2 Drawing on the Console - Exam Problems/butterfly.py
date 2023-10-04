n = int(input())
left_right = ((2 * n - 1) - 3) // 2
mid = "\\ /"
mid_bottom = "/ \\"

for row in range(n - 2):
    if row % 2 == 0:
        print("*" * left_right + mid + "*" * left_right)
    else:
        print("-" * left_right + mid + "-" * left_right)
print(" " * left_right + " @ " + " " * left_right)

for row in range(n - 2):
    if row % 2 == 0:
        print("*" * left_right + mid_bottom + "*" * left_right)
    else:
        print("-" * left_right + mid_bottom + "-" * left_right)
