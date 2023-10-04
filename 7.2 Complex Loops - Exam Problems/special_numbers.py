num = int(input())
last = 0
third = 0
second = 0
first = 0

for i in range(1111, 9999):
    first = i % 10
    second = i % 100 // 10
    third = i % 1000 // 100
    fourth = i // 1000
    if last > 0 and first > 0 and second > 0 and third > 0:
        if num % last == 0 and num % third == 0 and num % second == 0 and num % first == 0:
            print(i, end=" ")
    else:
        pass
