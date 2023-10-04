h = int(input())

x = int(input())
y = int(input())


if ((0 < x < h * 3) and h > y > 0) or ((h < x < h * 2) and (h < y < h * 4)):
    print("inside")
elif (h < x < h * 2) and y == h:
    print("inside")
elif ((0 <= x <= h * 3) and h >= y >= 0) or ((h <= x <= h * 2) and (h <= y <= h * 4)):
    print("border")
else:
    print("outside")