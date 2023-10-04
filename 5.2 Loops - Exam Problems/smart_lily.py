age = int(input())
w_m_price = float(input())
toy_price = int(input())
sum_collected = 0
money = 0

for i in range(1, age + 1):
    if i % 2 == 1:
        sum_collected += toy_price
    else:
        money += 10
        sum_collected += money
        sum_collected -= 1

if sum_collected >= w_m_price:
    print(f"Yes! {(sum_collected-w_m_price):.2f}")
else:
    print(f"No! {(abs(sum_collected - w_m_price)):.2f}")
