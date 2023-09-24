numbers = int(input())
left_sum = 0
right_sum = 0

for i in range(numbers):
    nums_left = float(input())
    left_sum += nums_left

for i in range(numbers):
    nums_right = float(input())
    right_sum += nums_right

if left_sum == right_sum:
    print(f"Yes, sum = {int(left_sum)}")
else:
    print(f"No, diff = {int(abs(left_sum-right_sum))}")