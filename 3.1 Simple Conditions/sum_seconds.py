p1 = int(input())
p2 = int(input())
p3 = int(input())

sum_secs = p1 + p2 + p3
mins = sum_secs // 60
secs = sum_secs % 60
if secs < 10:
    print(f"{mins}:0{secs}")
else:
    print(f"{mins}:{secs}")
