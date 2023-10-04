numbers = int(input())
max_num = - 999999999
sum_numbers = 0
for i in range(numbers):
    number = int(input())
    sum_numbers += number
    if number > max_num:
        max_num = number
if (sum_numbers-max_num) == max_num:
    print(f"Yes\nSum = {sum_numbers-max_num}")
else:
    print(f"No\nDiff = {abs(max_num-(sum_numbers-max_num))}")