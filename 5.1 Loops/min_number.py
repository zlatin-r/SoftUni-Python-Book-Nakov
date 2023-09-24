numbers = int(input())
min_number = 999999999999

for i in range(numbers):
    num = int(input())
    if num < min_number:
        min_number = num
print(min_number)