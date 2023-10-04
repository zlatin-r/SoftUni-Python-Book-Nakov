distance = float(input())
unit_input = input().lower()
unit_output = input().lower()

if unit_input == 'mm':
    distance = distance / 1000
elif unit_input == 'cm':
    distance = distance / 100
elif unit_input == 'mi':
    distance = distance / 0.000621371192
elif unit_input == 'in':
    distance = distance / 39.3700787
elif unit_input == 'km':
    distance = distance / 0.001
elif unit_input == 'ft':
    distance = distance / 3.2808399
elif unit_input == 'yd':
    distance = distance / 1.0936133

if unit_output == 'mm':
    distance = distance * 1000
elif unit_output == 'cm':
    distance = distance * 100
elif unit_output == 'mi':
    distance = distance * 0.000621371192
elif unit_output == 'in':
    distance = distance * 39.3700787
elif unit_output == 'km':
    distance = distance * 0.001
elif unit_output == 'ft':
    distance = distance * 3.2808399
elif unit_output == 'yd':
    distance = distance * 1.0936133

print(f"{distance} {unit_output}")
