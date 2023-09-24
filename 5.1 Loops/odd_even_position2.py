sum_even = 0
max_number_even = 'No'
min_number_even = 'No'

sum_odd = 0
max_number_odd = 'No'
min_number_odd = 'No'

n = int(input())
for number in range(1, n + 1):
    input_number = float(input())
    if number % 2 == 0:
        sum_even = input_number + sum_even
        if max_number_even == 'No' or input_number > max_number_even:
            max_number_even = input_number
        if min_number_even == 'No' or input_number < min_number_even:
            min_number_even = input_number
    else:
        sum_odd = input_number + sum_odd
        if max_number_odd == 'No' or input_number > max_number_odd:
            max_number_odd = input_number
        if min_number_odd == 'No' or input_number < min_number_odd:
            min_number_odd = input_number

print('OddSum={:,g},'.format(sum_odd))
if min_number_odd == 'No':
    print('OddMin={:},'.format(min_number_odd))
    print('OddMax={:},'.format(max_number_odd))
else:
    print('OddMin={:g},'.format(min_number_odd))
    print('OddMax={:g},'.format(max_number_odd))

print('EvenSum={:g},'.format(sum_even))
if min_number_even == 'No':
    print('EvenMin={:},'.format(min_number_even))
    print('EvenMax={:}'.format(max_number_even))
else:
    print('EvenMin={:g},'.format(min_number_even))
    print('EvenMax={:g}'.format(max_number_even))
