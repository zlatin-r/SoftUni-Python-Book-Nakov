import math
X = int(input())  # square meters yard
Y = float(input())  # grape for one square meter
Z = int(input())  # liters needed for vine
workers = int(input())

yard_for_vine = 0.4 * X
grape_for_vine = yard_for_vine * Y
liters_vine = grape_for_vine / 2.5
rest_vine = liters_vine - Z
vine_for_workers = rest_vine / workers

if liters_vine < Z:
    print(f"It will be a tough winter! More {math.floor(abs(rest_vine))} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {math.floor(liters_vine)} liters.")
    print(f"{math.ceil(rest_vine)} liters left -> {math.ceil(vine_for_workers)} liters per person.")
