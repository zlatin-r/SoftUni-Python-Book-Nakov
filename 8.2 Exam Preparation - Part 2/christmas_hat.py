n = int(input())

width = 4 * n + 1
high = 2 * n + 5

mid_part = high - 6

left_right = (width - 3) // 2
dashes = 1

print("." * left_right + "/|\\" + "." * left_right)
print("." * left_right + "\\|/" + "." * left_right)
print("." * left_right + "*" * 3 + "." * left_right)

for i in range(mid_part):
    left_right -= 1
    print(("." * left_right) + "*" + "-" * dashes + "*" + "-" * dashes + "*" + ("." * left_right))
    dashes += 1

print("*"*width)
print("*."*(width//2)+"*")
print("*"*width)
