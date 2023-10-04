chrysanthemums_count = int(input())
rouses_count = int(input())
tulips_count = int(input())
season = input().lower()
holiday = input()
total_flowers = chrysanthemums_count + rouses_count + tulips_count
chrysanthemums_price = 0
tulips_price = 0
rouses_price = 0
total_price = 0

if season == "spring" or season == "summer":
    chrysanthemums_price = 2 * chrysanthemums_count
    tulips_price = 2.50 * tulips_count
    rouses_price = 4.10 * rouses_count
elif season == "autumn" or season == "winter":
    chrysanthemums_price = 3.75 * chrysanthemums_count
    tulips_price = 4.15 * tulips_count
    rouses_price = 4.50 * rouses_count

total_price = chrysanthemums_price + tulips_price + rouses_price

if holiday == "Y":
    total_price += total_price * 0.15

if season == "spring" and tulips_count > 7:
    total_price -= (total_price * 0.05)

if season == "winter" and rouses_count >= 10:
    total_price -= (total_price * 0.10)

if total_flowers > 20:
    total_price -= (total_price * 0.20)

print(f"{total_price + 2:.2f}")
