import math
from math import fabs

holidays = int(input())

toms_norm = 30_000
working_days = 365 - holidays

total_play_minutes = working_days * 63 + holidays * 127
difference = math.fabs(total_play_minutes - toms_norm)

hours = int(difference // 60)
minutes = int(difference % 60)

if toms_norm > total_play_minutes:
    print(f"Tom sleeps well\n{hours} hours and {minutes} minutes less for play")
else:
    print(f"Tom will run away\n{hours} hours and {minutes} minutes more for play ")