amount = float(input())
currency_input = input()
currency_output = input()
result = 0

BGN = 1
USD = 1.79549
EUR = 1.95583
GBP = 2.53405

if currency_input == "BGN":
    amount *= BGN

elif currency_input == 'USD':
    amount *= USD

elif currency_input == 'EUR':
    amount *= EUR

elif currency_input == 'GBP':
    amount *= GBP

if currency_output == "BGN":
    result = amount / BGN

elif currency_output == "USD":
    result = amount / USD

elif currency_output == "EUR":
    result = amount / EUR

elif currency_output == "GBP":
    result = amount / GBP

print(f"{result:.2f} {currency_output}")
