month = input()
nights = int(input())

apartment = 0
studio = 0

if month == "May" or month == "October":
    if 7 < nights < 14:
        studio = (50 - (50 * 0.05)) * nights
        apartment = 65 * nights
    elif nights > 14:
        studio = (50 - (50 * 0.30)) * nights
        apartment = (65 - (65 * 0.10)) * nights
    else:
        studio = 50 * nights
        apartment = 65 * nights
elif month == "June" or month == "September":
    if nights > 14:
        studio = (75.20 - (75.20 * 0.20)) * nights
        apartment = (68.70 - (68.70 * 0.10)) * nights
    else:
        studio = 75.20 * nights
        apartment = 68.70 * nights
elif month == "July" or month == "August":
    if nights > 14:
        studio = 76 * nights
        apartment = (77 -(77 * 0.10)) * nights
    else:
        studio = 76 * nights
        apartment = 77 * nights
print(f"Apartment: {apartment:.2f} lv.\nStudio: {studio:.2f} lv.")
