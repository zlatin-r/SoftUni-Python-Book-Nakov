numbers = int(input())

odd_sum = 0.0
odd_min = 9999999999.9
odd_max = -9999999999.9
even_sum = 0.0
even_min = 9999999999.9
even_max = -99999999999.9

if numbers == 0:
    odd_min = "No"
    odd_max = "No"
    even_min = "No"
    even_max = "No"
elif numbers == 1:
    even_min = "No"
    even_max = "No"

for i in range(1, numbers + 1):
    nums = float(input())

    if i % 2 == 1:
        odd_sum += nums
        if nums < odd_min:
            odd_min = nums
        if nums > odd_max:
            odd_max = nums
    else:
        even_sum += nums
        if nums < even_min:
            even_min = nums
        if nums > even_max:
            even_max = nums

print(f"OddSum={odd_sum},\nOddMin={odd_min},\nOddMax={odd_max},"
      f"\nEvenSum={even_sum},\nEvenMin={even_min},\nEvenMax={even_max}")
print()
print("OddSum={:g},".format(odd_sum))
print("OddMin={:g},".format(odd_min))
print("OddMax={:g},".format(odd_max))
print("EvenSum={:g},".format(even_sum))
print("EvenMin={:g},".format(even_min))
print("EvenMax={:g}".format(even_max))
