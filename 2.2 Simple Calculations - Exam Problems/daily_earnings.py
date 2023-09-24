N_work_days_monthly = int(input())
M_salary_daily = float(input())
USD_BGN = float(input())


year_salary = (N_work_days_monthly * M_salary_daily) * 12

bonus_salary = (N_work_days_monthly * M_salary_daily) * 2.5

total_year_salary = (year_salary + bonus_salary)

salary_after_taxes = total_year_salary - (total_year_salary * 0.25)

daily_pay = (salary_after_taxes / 365)*USD_BGN

print(f"{daily_pay:.2f}")


