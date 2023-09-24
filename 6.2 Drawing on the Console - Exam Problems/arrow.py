n = int(input())

dots = n // 2
mid_dots = n - 2
hashes = n

print("." * dots + "#" * hashes + "." * dots)

for row in range(n - 2):
    print("." * dots + "#" + "." * mid_dots + "#" + "." * dots)
print("#" * (((n * 2 - 1) - mid_dots) // 2) + "." * mid_dots + "#" * (((n * 2 - 1) - mid_dots) // 2))

dots = 0
mid_dots = 2 * n - 5

for row in range(n - 2):
    dots += 1
    print("." * dots + "#" + "." * mid_dots + "#" + "." * dots)
    mid_dots -= 2
print("." * ((n * 2 - 1)//2) + "#" + "." * ((n * 2 - 1)//2))
