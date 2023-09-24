students = int(input())
students_count = 0
average_count = 0
low = 0
mid = 0
high = 0
best = 0

for i in range(students):
    grade = float(input())
    students_count += 1
    average_count += grade
    if 2.00 <= grade <= 2.99:
        low += 1
    elif 3.00 <= grade <= 3.99:
        mid += 1
    elif 4.00 <= grade <= 4.99:
        high += 1
    else:
        best += 1

print(f"Top students: {(best / students_count) * 100:.2f}%")
print(f"Between 4.00 and 4.99: {(high / students_count) * 100:.2f}%")
print(f"Between 3.00 and 3.99: {(mid / students_count) * 100:.2f}%")
print(f"Fail: {(low / students_count) * 100:.2f}%")
print(f"Average: {average_count/students_count:.2f}")
