n = int(input())
doctors = 7
checked_p = 0
unchecked_p = 0

for i in range(1, n + 1):
    patients = int(input())
    if i % 3 == 0 and unchecked_p > checked_p:
        doctors += 1

    if patients > doctors:
        unchecked_p += patients - doctors
        checked_p += doctors
    else:
        checked_p += patients

print(f"Treated patients: {checked_p}.")
print(f"Untreated patients: {unchecked_p}.")
