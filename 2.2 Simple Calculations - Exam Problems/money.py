bitcoins = int(input()) * 1168

CHY = (float(input()) * 0.15) * 1.76

tax = float(input())

total_amount = (bitcoins + CHY) / 1.95
total_amount_after_tax = total_amount - (total_amount * (tax / 100))
print(f"{total_amount_after_tax:.2f}")

