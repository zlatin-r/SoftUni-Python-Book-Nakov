budget = float(input())
season = input()

destination = ""
stays_in = ""
price = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == 'summer':
        stays_in = "Camp"
        price = budget * 0.30
    elif season == 'winter':
        price = budget * 0.70
        stays_in = "Hotel"
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == 'summer':
        stays_in = "Camp"
        price = budget * 0.40
    elif season == 'winter':
        stays_in = "Hotel"
        price = budget * 0.80
elif budget > 1000:
    destination = "Europe"
    stays_in = "Hotel"
    price = budget * 0.90
print(f"Somewhere in {destination}\n{stays_in} - {price:.2f}")