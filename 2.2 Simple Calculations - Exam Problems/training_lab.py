l = float(input())*100
w = float(input())*100

rows = l // 120
columns = (w-100) // 70

work_places = (rows * columns)-3

print(round(work_places))
