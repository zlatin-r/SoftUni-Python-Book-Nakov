km = int(input())
time = input()
price = 0
taxi_rate = 0

if time == "day":
    taxi_rate = 0.79
else:
    taxi_rate = 0.90

if km < 20:
    price = 0.70 + km * taxi_rate
elif km < 100:
    price = km * 0.09
else:
    price = km * 0.06

print(f"{price:.2f}")