d = int(input())
m = int(input())

day_in_month = 31

if m == 2:
    day_in_month = 28

if m == 4 or m == 6 or m == 9 or m == 11:
    day_in_month = 30

d += 5

if d > day_in_month:
    d -= day_in_month
    m += 1

    if m > 12:
        m = 1

print("%d.%02d" % (d, m))
