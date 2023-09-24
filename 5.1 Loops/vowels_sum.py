word = input()
summ = 0

for i in word:
    if i == "a":
        summ += 1
    elif i == "e":
        summ += 2
    elif i == "i":
        summ += 3
    elif i == "o":
        summ += 4
    elif i == "u":
        summ += 5
print(summ)