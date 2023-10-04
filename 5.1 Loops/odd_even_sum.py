numbers = int(input())
evens = 0
odds = 0

for i in range(numbers):
    number = int(input())
    if i % 2 == 0:
        evens += number
    else:
        odds += number

if evens == odds:
    print(f"Yes\nSum = {evens}")
else:
    print(f"No\nDiff = {int(abs(evens-odds))}")