budget = float(input())
category = input()
group = int(input())
tickets = 0
transport_price = 0

if category == "VIP":
    tickets = 499.99 * group
elif category == "Normal":
    tickets = 249.99 * group

if group <= 4:
    transport_price = budget * 0.75
elif group <= 9:
    transport_price = budget * 0.60
elif group <= 24:
    transport_price = budget * 0.50
elif group <= 49:
    transport_price = budget * 0.40
elif 50 <= group:
    transport_price = budget * 0.25

difference = budget - (transport_price + tickets)
if difference > 0:
    print(f"Yes! You have {difference:.2f} leva left.")
elif difference < 0:
    print(f"Not enough money! You need {abs(difference):.2f} leva.")