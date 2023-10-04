product = input().lower()
city = input().lower()
amount = float(input())

if city == 'sofia':
    if product == "coffee":
        print(0.50 * amount)
    elif product == "water":
        print(0.80 * amount)
    elif product == "beer":
        print(1.20 * amount)
    elif product == "sweets":
        print(1.45 * amount)
    elif product == "peanuts":
        print(1.60 * amount)
if city == 'plovdiv':
    if product == "coffee":
        print(0.40 * amount)
    elif product == "water":
        print(0.70 * amount)
    elif product == "beer":
        print(1.15 * amount)
    elif product == "sweets":
        print(1.30 * amount)
    elif product == "peanuts":
        print(1.50 * amount)
if city == 'varna':
    if product == "coffee":
        print(0.45 * amount)
    elif product == "water":
        print(0.70 * amount)
    elif product == "beer":
        print(1.10 * amount)
    elif product == "sweets":
        print(1.35 * amount)
    elif product == "peanuts":
        print(1.55 * amount)
