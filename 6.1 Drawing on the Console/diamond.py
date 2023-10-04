n = int(input())

mid_dashes_top = 0
mid_dashes_bottom = n - 4

is_even = n % 2 == 0

if is_even:
    dashes = int((n - 2) / 2)
    stars = 2

else:
    dashes = int(n / 2)
    stars = 1

if n <= 2:
    print("-" * dashes + "*" * stars + "-" * dashes)

elif is_even and n > 2:
    print("-" * dashes + "*" * stars + "-" * dashes)

    for row in range(1, int(n / 2)):
        mid_dashes_top += 1
        print("-" * (dashes - row) + "*" + "-" * (mid_dashes_top + row) + "*" + "-" * (dashes - row))

    for row in range(int(n / 2), n - 2):
        print("-" * (row - dashes) + "*" + "-" * mid_dashes_bottom + "*" + "-" * (row - dashes))
        mid_dashes_bottom -= 2
    print("-" * dashes + "*" * stars + "-" * dashes)

else:
    print("-" * dashes + "*" * stars + "-" * dashes)
    for row in range(1, int(n / 2) + 1):
        print("-" * (dashes - row) + "*" + "-" * (mid_dashes_top + 1) + "*" + "-" * (dashes - row))
        mid_dashes_top += 2

    for row in range(int(n / 2), n - 2):
        print("-" * (row - dashes + 1) + "*" + "-" * mid_dashes_bottom + "*" + "-" * (row - dashes + 1))
        mid_dashes_bottom -= 2
    print("-" * dashes + "*" * stars + "-" * dashes)