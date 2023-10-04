N = float(input())
W = float(input())
L = float(input())
M = float(input())
O = float(input())
time = 0.2

area_size = N*N
tiles_size = W * L
bench_size = M * O

total_area = area_size - bench_size
tiles_needed = total_area / tiles_size
total_time = tiles_needed * time

print(f"{tiles_needed:.2f}")
print(f"{total_time:.2f}")
