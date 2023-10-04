speed = int(input())
time_1 = int(input())
time_2 = int(input())
time_3 = int(input())

time_1 /= 60
distance_1 = speed * time_1

time_2 /= 60
speed_2 = speed + (speed * 0.10)
distance_2 = speed_2 * time_2

time_3 /= 60
speed_3 = speed_2 - (speed_2 * 0.05)
distance_3 = speed_3 * time_3

distance = distance_1 + distance_2 + distance_3

print(f"{distance:.2f}")
