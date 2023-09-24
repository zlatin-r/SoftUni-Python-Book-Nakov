projection = input().lower()
rows = int(input())
col = int(input())

total_win = 0

if projection == 'premiere':
    total_win = (rows * col) * 12
elif projection == 'normal':
    total_win = (rows * col) * 7.50
elif projection == 'discount':
    total_win = (rows * col) * 5

print(f"{total_win:.2f}")
