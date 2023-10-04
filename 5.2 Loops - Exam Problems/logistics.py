n = int(input())

bus = 0
truck = 0
train = 0
count_bus = 0
count_truck = 0
count_train = 0

for i in range(1, n + 1):
    weight = int(input())
    if weight <= 3:
        bus += weight
        count_bus += 1
    if 3 < weight <= 11:
        truck += weight
        count_truck += 1
    if weight > 11:
        train += weight
        count_train += 1

all_cargo = bus + truck + train
avrg_price = ((bus * 200) + (truck * 175) + (train * 120)) / all_cargo

print(f"{avrg_price:.2f}")
print(f"{(bus / all_cargo) * 100:.2f}%")
print(f"{(truck / all_cargo) * 100:.2f}%")
print(f"{(train / all_cargo) * 100:.2f}%")
