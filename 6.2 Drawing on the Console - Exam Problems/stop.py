n = int(input())

dots = n + 1
underscores = 2 * n + 1
mid = underscores - 2

print("." * dots + "_" * underscores + "." * dots)
for row in range(n):
    dots -= 1
    print("." * dots + "//" + "_" * mid + "\\\\" + "." * dots)
    mid += 2
print("//" + "_" * ((mid - 5) // 2) + "STOP!" + "_" * ((mid - 5) // 2) + "\\\\")
print("\\\\" + "_" * mid + "//")
dots = 0
mid -= 2
for row in range(1, n):
    dots += 1
    print("." * dots + "\\\\" + "_" * mid + "//" + "." * dots)
    mid -= 2
