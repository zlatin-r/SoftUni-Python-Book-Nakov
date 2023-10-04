import math
budget = float(input())
width_floor = float(input())
length_floor = float(input())
side_triangle = float(input())
height_triangle = float(input())
price_tile = float(input())
worker_price = float(input())

area_floor = width_floor * length_floor
area_tile = side_triangle * height_triangle / 2
tile_needed = (area_floor / area_tile) + 5
money_needed = (math.ceil(tile_needed) * price_tile) + worker_price

if money_needed <= budget:
    print(f"{budget-money_needed:.2f} lv left.")
else:
    print(f"You'll need {abs(budget-money_needed):.2f} lv more.")
