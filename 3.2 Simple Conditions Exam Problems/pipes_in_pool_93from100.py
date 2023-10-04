V = int(input())
P1 = int(input())
P2 = int(input())
H = float(input())


water = (P1 + P2) * H

if water <= V:
    pool_fullness = int(water / V * 100)
    pipe1_percentage = int(P1 * H / water * 100)
    pipe2_percentage = int(P2 * H / water * 100)
    print(f"The pool is {pool_fullness}% full. Pipe 1: {pipe1_percentage}%. Pipe 2: {pipe2_percentage}%.")
else:
    overflow = water - V
    print(f"For {H} hours the pool overflows with {overflow:.1f} liters.")

