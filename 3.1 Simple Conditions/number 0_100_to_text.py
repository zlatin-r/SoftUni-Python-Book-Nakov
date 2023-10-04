num = int(input())

if num < 0 or num > 100:
    print("Number out of range.")
if num == 0:
    print("zero")
if num == 100:
    print("one hundred")

ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

if 0 < num < 10:
    print(ones[num - 1])

elif num == 10:
    print(tens[0])

elif 10 < num < 20:
    print(teens[num % 10 - 1])

elif 100 > num >= 20:
    if num % 10 == 0:
        print(tens[num // 10 - 1])
    else:
        print(tens[num // 10 - 1] + " " + ones[num % 10 - 1])