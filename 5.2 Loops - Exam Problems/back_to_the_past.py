inheritance = float(input())
year = int(input())
money_spend = 0
years_count = 17

for i in range(1800, year + 1):
    years_count += 1
    if i % 2 == 0:
        inheritance -= 12000
    else:
        inheritance -= 12000 + 50 * years_count

if inheritance >= money_spend:
    print(f"Yes! He will live a carefree life and will have {inheritance:.2f} dollars left.")
else:
    print(f"He will need {abs(inheritance):.2f} dollars to survive.")