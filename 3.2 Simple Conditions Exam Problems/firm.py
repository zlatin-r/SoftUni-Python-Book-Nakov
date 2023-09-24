import math

project_hours = int(input())
available_days = int(input()) * 0.90
employees = int(input())

available_work_hours = (available_days * 8) * employees + (employees * 2) * available_days

if available_work_hours >= project_hours:
    print(f"Yes!{math.floor(available_work_hours - project_hours)} hours left.")
else:
    print(f"Not enough time!{math.floor(abs(available_work_hours - project_hours))} hours needed.")

