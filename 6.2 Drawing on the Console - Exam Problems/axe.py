n = int(input())

left_dashes = n * 3
right_dashes = (5 * n) - left_dashes - 2
mid_dashes = 1
stars = n * 3

print("-" * left_dashes + "**" + "-" * right_dashes)

for row in range(n - 1):
    print("-" * left_dashes + "*" + "-" * mid_dashes + "*" + "-" * (right_dashes - mid_dashes))
    mid_dashes += 1
mid_dashes -= 1

for row in range(n // 2):
    print("*" * stars + "*" + "-" * mid_dashes + "*" + "-" * (right_dashes - mid_dashes))

for row in range(1,n // 2):
    print("-" * left_dashes + "*" + "-" * mid_dashes + "*" + "-" * (right_dashes - mid_dashes))
    left_dashes -= 1
    right_dashes += 1
    mid_dashes += 2

print("-" * left_dashes + "*" + "*" * mid_dashes + "*" + "-" * (right_dashes - mid_dashes))